import os
import torch
import pandas as pd
import streamlit as st
from transformers import AutoTokenizer
from transformers import DistilBertForSequenceClassification
from utils.preprocess import basic_preprocess
from utils.visuals import plot_most_common_features

def show():
    st.title("📰 Full-Year News Sentiment Overview (BERT Model)")

    # ✅ Load BERT model
    model_path = "models/bert_sentiment_model"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = DistilBertForSequenceClassification.from_pretrained(model_path)
    model.eval()

    # ✅ Label map
    label_map = {0: "negative", 1: "neutral", 2: "positive"}

    @st.cache_data(show_spinner=False)
    def predict_sentiment_bert(text_list, batch_size=32):
        results = []
        for i in range(0, len(text_list), batch_size):
            batch = text_list[i:i + batch_size]
            inputs = tokenizer(batch, padding=True, truncation=True, return_tensors="pt", max_length=256)
            with torch.no_grad():
                outputs = model(**inputs)
                preds = torch.argmax(outputs.logits, dim=1).tolist()
            results.extend([label_map[p] for p in preds])
        return results

    # ✅ Load and preprocess news data
    df = pd.read_csv("data/NewsData_cleaned.csv")
    df["pubDate"] = pd.to_datetime(df["pubDate"], errors="coerce")
    df["clean_title"] = df["title"].astype(str).apply(basic_preprocess)

    # ✅ Predict for latest date
    latest_date = df["pubDate"].max().date()
    latest_df = df[df["pubDate"].dt.date == latest_date].copy()

    with st.spinner("🔄 Running predictions using fine-tuned BERT on latest headlines..."):
        latest_df["sentiment"] = predict_sentiment_bert(latest_df["clean_title"].tolist())

    # ✅ Stats and charts
    st.markdown(f"**Total Articles Analyzed:** {len(latest_df)}")
    st.markdown(f"**Latest Date in Dataset:** `{latest_date}`")

    st.subheader("Sentiment Distribution")
    sentiment_counts = latest_df["sentiment"].value_counts()
    st.bar_chart(sentiment_counts)

    # ✅ Load full-year data for keyword chart
    keyword_df = pd.read_csv("data/df_en_clean.csv")
    keyword_df["clean_title"] = keyword_df["clean_title"].astype(str)
    keyword_df["sentiment"] = keyword_df["sentiment"].astype(str)

    st.subheader("Top Keywords Across All News")
    plot_most_common_features(keyword_df["clean_title"], keyword_df["sentiment"])
