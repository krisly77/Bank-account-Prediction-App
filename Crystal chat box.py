import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')
nltk.download('average_perception_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st