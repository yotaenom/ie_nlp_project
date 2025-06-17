import sys
import os
sys.path.append(os.path.dirname(__file__))

import nltk
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

import streamlit as st
from custom_pages import overview, sentiment, forecast

# Set Streamlit page settings
st.set_page_config(page_title="Tesla NLP Dashboard", layout="wide")

# Apply custom CSS for sidebar and nav buttons
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background: linear-gradient(to bottom right, #ffffff, #f2f2f2);
        padding: 2rem 1rem;
    }
    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 20px;
        padding-left: 6px;
        color: #333;
    }
    .avatar-icon {
        text-align: center;
        font-size: 32px;
        margin-bottom: 20px;
    }
    .nav-btn {
        background-color: #f2f2f2;
        border: none;
        padding: 12px 16px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 14px;
        width: 100%;
        margin-bottom: 10px;
        transition: all 0.25s ease;
        text-align: left;
        color: #333;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .nav-btn:hover {
        transform: scale(1.03);
        background-color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }
    .nav-btn.active {
        background-color: #ff4b4b !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Tesla logo section
st.sidebar.markdown("""
    <div style='text-align: center; margin-bottom: 20px; margin-top: -50px;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Tesla_Motors.svg/512px-Tesla_Motors.svg.png' width='100'/>
        <div style='font-size:16px; font-weight:600; margin-top: 10px; margin-bottom: 50px; color:#333;'></div>
    </div>
""", unsafe_allow_html=True)

# Navigation logic
pages = {
    "Overview 2📄": overview,
    "Predict News Sentiment 🗞️": sentiment,
    "Stock Direction Prediction 📈": forecast,
}

if "current_page" not in st.session_state:
    st.session_state.current_page = list(pages.keys())[0]

# Styled nav buttons
for label in pages.keys():
    is_active = "active" if label == st.session_state.current_page else ""
    if st.sidebar.button(label, key=label, use_container_width=True):
        st.session_state.current_page = label

# Show selected page
pages[st.session_state.current_page].show()