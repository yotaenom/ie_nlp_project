import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os
import yfinance as yf
from datetime import datetime, timedelta

def load_tsla_cached(start_date, end_date, cache_path="data/tsla_cached.csv"):
    if os.path.exists(cache_path):
        tsla = pd.read_csv(cache_path, parse_dates=["Date"])
    else:
        tsla = yf.download("TSLA", start=start_date, end=end_date, interval="1d")
        tsla.columns = tsla.columns.get_level_values(0) if isinstance(tsla.columns, pd.MultiIndex) else tsla.columns
        tsla.reset_index(inplace=True)
        tsla.to_csv(cache_path, index=False)
    return tsla

def show():
    st.title("📈 Tesla Stock Direction Forecast")
    st.subheader("TSLA Price Movement (6 Months Before 2025-01-15)")

    # --- Download and show price chart ---
    end_date = datetime(2025, 1, 15)
    start_date = end_date - timedelta(days=180)

    tsla = load_tsla_cached(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
    plt.figure(figsize=(10, 4))
    plt.plot(tsla['Date'], tsla['Close'], label='TSLA Close Price')
    plt.title('Tesla (TSLA) - 6 Months Before 2025-01-15')
    plt.xlabel('Date')
    plt.ylabel('Close Price ($)')
    plt.legend()
    st.pyplot(plt)

    st.subheader("🧠 Model Prediction for Next Day")

    # --- Load news data ---
    df = pd.read_csv("data/NewsData_cleaned.csv")
    df['pubDate'] = pd.to_datetime(df['pubDate'])
    df['pubDate_day'] = df['pubDate'].dt.date

    # --- Download full TSLA data or use cached ---
    tsla_full = load_tsla_cached("2024-01-01", "2025-01-16", cache_path="data/tsla_full_cached.csv")
    tsla_full["Date"] = pd.to_datetime(tsla_full["Date"]).dt.date

    # --- Merge ---
    df["pubDate_day"] = pd.to_datetime(df["pubDate_day"])
    tsla_full["Date"] = pd.to_datetime(tsla_full["Date"])
    merged = df.merge(tsla_full, left_on="pubDate_day", right_on="Date", how="left")
    merged = merged[["pubDate", "sentiment", "Open", "High", "Low", "Close", "Volume"]].dropna()
    merged["sentiment"] = merged["sentiment"].str.strip('"')

    # --- Sentiment encoding ---
    merged["pos"] = (merged["sentiment"] == "positive").astype(int)
    merged["neg"] = (merged["sentiment"] == "negative").astype(int)
    merged["neu"] = (merged["sentiment"] == "neutral").astype(int)
    merged["date"] = merged["pubDate"].dt.floor("D")

    # --- Feature engineering ---
    sentiment_daily = merged.groupby("date")[["pos", "neg", "neu"]].sum()
    prices_daily = merged.groupby("date")[["Open", "High", "Low", "Close", "Volume"]].first()
    features = pd.concat([prices_daily, sentiment_daily], axis=1)
    features["target"] = (features["Close"].shift(-1) > features["Close"]).astype(int)
    features["return_1d"] = features["Close"].pct_change()
    features["volatility_3d"] = features["Close"].pct_change().rolling(3).std()
    features["momentum_3d"] = features["Close"] - features["Close"].shift(3)
    total = features[["pos", "neg", "neu"]].sum(axis=1)
    features["sentiment_score"] = (features["pos"] - features["neg"]) / total.replace(0, 1)
    features["Close_lag1"] = features["Close"].shift(1)
    features["pos_lag1"] = features["pos"].shift(1)
    features.dropna(inplace=True)

    # --- Load model and predict ---
    model = joblib.load("models/xgb_direction_model.pkl")
    booster = model.get_booster()
    expected_features = booster.feature_names
    X_latest = features[expected_features] if set(expected_features).issubset(features.columns) else features[[f for f in expected_features if f in features.columns]]

    prediction = model.predict(X_latest.tail(1))[0]
    direction = "📈 Up" if prediction == 1 else "📉 Down"
    st.metric("2025-01-16 Prediction", direction)
