import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Set persistent NLTK data directory
nltk_data_path = os.path.expanduser("~/nltk_data")
nltk.data.path.append(nltk_data_path)

# Define required packages with corpus paths
required_packages = [
    ("corpora/wordnet", "wordnet"),
    ("corpora/stopwords", "stopwords"),
    ("taggers/averaged_perceptron_tagger", "averaged_perceptron_tagger"),
    ("corpora/omw-1.4", "omw-1.4"),
]

# Download missing packages only
for corpus_path, package in required_packages:
    try:
        nltk.data.find(corpus_path)
    except LookupError:
        nltk.download(package, download_dir=nltk_data_path)

# Initialize NLP components
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
