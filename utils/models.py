import joblib
import pickle

def load_sentiment_model():
    model = joblib.load("models/logistic_model.pkl")
    vectorizer = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))
    label_encoder = pickle.load(open("models/label_encoder.pkl", "rb"))
    return model, vectorizer, label_encoder

def load_forecast_model():
    return joblib.load("models/xgb_direction_model.pkl")
