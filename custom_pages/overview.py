import streamlit as st

def show():
    # --- CSS Styling ---
    st.markdown("""
        <style>
            .main-title {
                font-size: 40px;
                text-align: center;
                font-weight: 800;
                color: black;
                margin-bottom: -5px;
                margin-top: -10px;
            }
            .subtitle {
                font-size: 18px;
                text-align: center;
                color: #666;
                margin-top: 15px;
                margin-bottom: 30px;
            }
            .hover-block {
                transition: all 0.3s ease;
                padding: 15px 20px;
                border-radius: 12px;
                margin-bottom: 12px;
                background-color: #f0f2f6;
                box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            }
            .hover-block:hover {
                transform: scale(1.03);
                background-color: white;
                box-shadow: 0 4px 14px rgba(0,0,0,0.08);
            }
            .hover-title {
                font-weight: 600;
                font-size: 17px;
                color: #222;
                margin-bottom: 5px;
            }
            .hover-desc {
                font-size: 15px;
                color: #555;
            }
            .dev-grid {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 16px;
                margin-top: 10px;
            }
            .dev-box {
                flex: 0 1 calc(45% - 10px);
                min-width: 200px;
                background-color: #f0f2f6;
                padding: 15px 20px;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.04);
                text-align: center;
                font-weight: 600;
                font-size: 17px;
                color: #222;
                transition: all 0.3s ease;
            }
            .dev-box:hover {
                transform: scale(1.03);
                background-color: white;
                box-shadow: 0 4px 14px rgba(0,0,0,0.08);
            }
        </style>
    """, unsafe_allow_html=True)

    # --- Title + Subtitle ---
    st.markdown("<div class='main-title'>News-Based Sentiment Prediction & Stock Forecasting</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>An NLP-Powered Dashboard to Decode Market Sentiment</div>", unsafe_allow_html=True)

    # --- Tab Navigation ---
    tab_names = ["Objective", "Technologies", "App Features", "Importance", "Developed By"]
    if "selected_tab" not in st.session_state:
        st.session_state.selected_tab = tab_names[0]

    cols = st.columns(len(tab_names), gap="small")
    for i, tab in enumerate(tab_names):
        with cols[i]:
            if st.button(tab, key=tab, use_container_width=True):
                st.session_state.selected_tab = tab

    tab = st.session_state.selected_tab

    # --- Tab Content ---
    if tab == "Objective":
        st.markdown("""
            <div class='hover-block'>
                <div class='hover-title'>📰 TSLA News Coverage</div>
                <div class='hover-desc'>Analyze daily headlines and descriptions related to Tesla (TSLA) using natural language processing.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🎯 Sentiment Classification</div>
                <div class='hover-desc'>Leverage a fine-tuned DistilBERT model to classify article sentiment into 🟢 <b>Positive</b>, 🟣 <b>Neutral</b>, 🔴 <b>Negative</b>.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📈 Price Pattern Linkage</div>
                <div class='hover-desc'>Forecast next-day stock direction based on sentiment trends and historical price indicators.</div>
            </div>
        """, unsafe_allow_html=True)

    elif tab == "Technologies":
        st.markdown("""
            <div class='hover-block'>
                <div class='hover-title'>🧠 DistilBERT (Transformers)</div>
                <div class='hover-desc'>Used a fine-tuned DistilBERT model for highly accurate sentiment classification on TSLA news data.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📊 XGBoost Classifier</div>
                <div class='hover-desc'>Applied for binary classification of next-day TSLA stock direction based on engineered features.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📈 yFinance</div>
                <div class='hover-desc'>Fetched historical TSLA price data and aligned it with daily sentiment scores.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📦 Joblib & Pickle</div>
                <div class='hover-desc'>Used for saving/loading ML models and ensuring efficient deployment across modules.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🌐 Streamlit</div>
                <div class='hover-desc'>Framework for building an interactive dashboard with custom layout and navigation controls.</div>
            </div>
        """, unsafe_allow_html=True)

    elif tab == "App Features":
        st.markdown("""
            <div class='hover-block'>
                <div class='hover-title'>🔍 Daily Sentiment Scan</div>
                <div class='hover-desc'>Applies DistilBERT to classify all TSLA headlines for the latest available day.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📊 Sentiment Distribution</div>
                <div class='hover-desc'>Interactive bar chart displays how news is classified into positive, neutral, or negative classes.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🧠 Keyword Insights</div>
                <div class='hover-desc'>Extracts and visualizes key terms driving each sentiment label for transparency and explainability.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📈 Stock Forecasting</div>
                <div class='hover-desc'>Leverages XGBoost to predict next-day TSLA price direction based on sentiment and technical indicators.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🧼 End-to-End Pipeline</div>
                <div class='hover-desc'>From raw headline ingestion to market prediction, fully automated in a single dashboard.</div>
            </div>
        """, unsafe_allow_html=True)

    elif tab == "Importance":
        st.markdown("""
            <div class='hover-block'>
                <div class='hover-title'>📰 The Power of News</div>
                <div class='hover-desc'>Headlines drive investor sentiment and market volatility in real time.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📣 From Information to Impact</div>
                <div class='hover-desc'>This app turns Tesla news into structured, actionable market signals.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📈 Linking Media to Price</div>
                <div class='hover-desc'>Lays the foundation for correlating sentiment with TSLA price behavior.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🤖 Smarter Decision-Making</div>
                <div class='hover-desc'>Helps investors and analysts react faster to news-based sentiment swings.</div>
            </div>
        """, unsafe_allow_html=True)

    elif tab == "Developed By":
        st.markdown("""
            <div class='dev-grid'>
                <div class='dev-box'>🧠 Samir Barakat</div>
                <div class='dev-box'>📊 Yotaro Enomoto</div>
                <div class='dev-box'>🛠️ Omar Althwaini</div>
                <div class='dev-box'>🧮 Omar Harradi</div>
                <div class='dev-box'>🔬 Edwin Blanco</div>
                <div class='dev-box'>📈 Halil Can Kuloglu</div>
            </div>
        """, unsafe_allow_html=True)
