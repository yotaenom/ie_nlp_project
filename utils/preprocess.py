import re
from nltk import pos_tag
from nltk.corpus import wordnet
from utils.config import lemmatizer, stop_words

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith("J"):
        return wordnet.ADJ
    elif treebank_tag.startswith("V"):
        return wordnet.VERB
    elif treebank_tag.startswith("N"):
        return wordnet.NOUN
    elif treebank_tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def basic_preprocess(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = text.split()
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    tagged = pos_tag(tokens, lang='eng')
    lemmatized = [lemmatizer.lemmatize(w, get_wordnet_pos(pos)) for w, pos in tagged]
    return " ".join([w for w in lemmatized if len(w) > 1])
