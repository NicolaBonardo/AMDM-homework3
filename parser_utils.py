# Utilities for parser.py
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import string
#from nltk.stem import PorterStemmer
import utils

stop_words = set(stopwords.words('english'))
translate_table = dict((ord(char), None) for char in string.punctuation)

def preprocess(text):
    text = text.replace('\n', '')
    text = text.translate(translate_table)
    tokens = word_tokenize(text)  
    filtered_text = [w for w in tokens if not w in stop_words]

    #ps = PorterStemmer()    
    #stemmed = [ps.stem(word) for word in filtered_text]
    stemmed = utils.stemList(filtered_text)
    
    result = ' '.join(stemmed)
    return(result)
