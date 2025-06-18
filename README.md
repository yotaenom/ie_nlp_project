# Tesla Stock Prediction Using News and NLP
![Tesla News/Stocks](https://media.assettype.com/analyticsinsight%2F2024-08-26%2Ftsgr2q18%2FIs-It-Time-to-Buy-or-Sell-Tesla-Stock.jpg)

This project applies Natural Language Processing (NLP) and machine learning models to forecast Tesla stock movements using news sentiment and historical data.

### Key features:
- Sentiment classification (positive, negative, neutral) of news headlines using a BERT model  
- Stock movement prediction using logistic regression and XGBoost  
- Integration of textual sentiment and time-aligned stock price data  
- Streamlit-based interactive dashboard

### Models used:
1. **BERT** – Fine-tuned for sentiment classification  
2. **Logistic Regression** – Predicts next-day stock direction  
3. **XGBoost** – Captures non-linear trends in stock movement  
4. **TF-IDF** – Extracts relevant features from cleaned news text  

---

## Setup

#### 1. Clone this repository  
#### 2. Create and activate virtual environment
```bash
conda create -n nlp_stock python=3.12 pip
conda activate nlp_stock
pip install -r requirements.txt
```

#### 3. Install PyTorch  
Follow installation instructions here: https://pytorch.org/get-started/locally/

#### 4. Download models and datasets  
All necessary data and model files can be downloaded from the [Google Drive folder](https://drive.google.com/drive/folders/1r9zYwbNwVLXuDjrhU8aQvhXdNaurs4Ox?usp=sharing).  
Extract them into the appropriate `models/` and `data/` directories.

---

## File Structure
```
├── custom_pages/
│   ├── forecast.py           # Prediction logic and Streamlit page
│   ├── overview.py           # Project overview
│   ├── sentiment.py          # Sentiment analysis page
│   └── __init__.py
│
├── data/                     # News and stock datasets
│   
├── eda/                      # Final EDA notebook
├── eda_old/                  # Intermediate EDA notebooks
├── main.py                   # App entry point
│
├── models/
│
├── utils/                    # Helper functions
│   ├── config.py
│   ├── models.py
│   ├── preprocess.py
│   └── visuals.py
│
├── requirements.txt
└── README.md
```

---

## Running the App
Make sure you’ve downloaded the model files and datasets. Then, run:
```bash
streamlit run main.py
```

This will launch a browser-based dashboard with multiple tabs:
- **Overview**: Project motivation and summary  
- **Sentiment**: Live sentiment classification results  
- **Forecast**: Stock prediction results using selected models

---

## Notes
- For full functionality, make sure the model paths in `utils/config.py` are correctly set.
- Model training was conducted offline. This app runs inference only.
- If facing memory issues, consider simplifying inputs or switching to CPU mode.

---

## Collaborators
**EDWIN ABBOUD BLANCO**, **OMER ALTHWAINI**, **SAMIR BARAKAT**, **YOTARO ENOMOTO**, **OMAR HARRADI**, **HALIL CAN KULOGLU**
