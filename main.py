import sys
import os
sys.path.append(os.path.dirname(__file__))
import nltk
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("punkt")  
nltk.download("stopwords")  
nltk.download("wordnet")  # 


import streamlit as st
from custom_pages import overview, sentiment, forecast

st.set_page_config(page_title="Tesla NLP Dashboard", layout="wide")

pages = {
    "Overview 2📄": overview,
    "Predict News Sentiment 🗞️": sentiment,
    "Stock Direction Prediction 📈": forecast,
}

# Sidebar UI
st.sidebar.markdown("""
    <div style='text-align: center; margin-bottom: 20px;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Tesla_Motors.svg/512px-Tesla_Motors.svg.png' width='100'/>
    </div>
    <hr style="margin-top:0;margin-bottom:10px;">
""", unsafe_allow_html=True)

selection = st.sidebar.radio("📌 Navigation", list(pages.keys()))
pages[selection].show()
