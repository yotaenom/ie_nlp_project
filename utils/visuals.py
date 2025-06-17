import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from nltk.tokenize import WhitespaceTokenizer

def plot_most_common_features(text_col, target_col, n_features=50):
    df = pd.DataFrame({"text": text_col, "CLASS": target_col})
    grouped = df.groupby("CLASS").apply(lambda x: x["text"].sum())
    grouped_df = pd.DataFrame({"CLASS": grouped.index, "text": grouped.values})
    tokenizer = WhitespaceTokenizer()
    for ii, text in enumerate(grouped_df.text):
        pd.DataFrame(tokenizer.tokenize(text))\
            .apply(pd.value_counts).head(n_features).plot(kind="bar", figsize=(20,5))
        plt.title(grouped_df.CLASS[ii], fontsize=20)
        plt.xticks(fontsize=15)
        plt.legend([])
        st.pyplot(plt)
