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
                <div class='hover-desc'>Analyze a full year of Tesla (TSLA) news articles to extract insights from headlines.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🎯 Sentiment Classification</div>
                <div class='hover-desc'>Classify article sentiment using ML: 🟢 <b>Positive</b>, 🟣 <b>Neutral</b>, 🔴 <b>Negative</b>.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📈 Price Pattern Linkage</div>
                <div class='hover-desc'>Establish a foundation for correlating sentiment trends with TSLA stock price movements.</div>
            </div>
        """, unsafe_allow_html=True)

    elif tab == "Technologies":
        st.markdown("""
            <div class='hover-block'>
                <div class='hover-title'>💻 Python & Streamlit</div>
                <div class='hover-desc'>Used to build the interactive web application and user interface.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🧹 NLTK Preprocessing</div>
                <div class='hover-desc'>Handles tokenization, lemmatization, and stopword removal for text cleaning.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📊 TF-IDF Vectorizer</div>
                <div class='hover-desc'>Converts cleaned headlines into numerical features representing word importance.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🤖 Logistic Regression</div>
                <div class='hover-desc'>Trained ML model to classify sentiment into Positive, Neutral, or Negative.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🗂️ Pickle & Joblib</div>
                <div class='hover-desc'>Used for saving, loading, and deploying the trained model assets efficiently.</div>
            </div>
        """, unsafe_allow_html=True)

    elif tab == "App Features":
        st.markdown("""
            <div class='hover-block'>
                <div class='hover-title'>🔍 Headline Prediction</div>
                <div class='hover-desc'>Automatically classifies all news articles by sentiment.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>📊 Sentiment Chart</div>
                <div class='hover-desc'>Interactive bar chart showing sentiment distribution over time.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🧠 Keyword Insights</div>
                <div class='hover-desc'>Highlights relevant keywords per sentiment class for explainability.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🧼 End-to-End Automation</div>
                <div class='hover-desc'>From preprocessing to prediction in one pipeline with minimal user effort.</div>
            </div>
            <div class='hover-block'>
                <div class='hover-title'>🔗 Modular Design</div>
                <div class='hover-desc'>Future-ready structure for adding stock movement prediction and more.</div>
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
