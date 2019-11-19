# Utilities
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
import math

downloaded_dir = "C:\\Users\\nbonardo\\movies"

def getMovieTitle(docId):
    fileName = downloaded_dir + "\\article_" + str(docId) + ".html"

    with open(fileName, encoding="utf-8") as html_file:
        soup = BeautifulSoup(html_file, 'lxml')

    title = soup.title.text
    title = title.replace("- Wikipedia", "")
    return(title)

# method used to stem a list of words
# used both in parser.py and in main.py
def stemList(listOfWords):
    ps = PorterStemmer()    
    stemmed = [ps.stem(word) for word in listOfWords]
    return(stemmed)

def scalarProd(dictA, dictB):
    msum = 0
    for key in dictA:
        msum += dictA[key] * dictB[key]
    return(msum)

def cosine(dictA, dictB):
    lenA = math.sqrt(scalarProd(dictA, dictA))    
    lenB = math.sqrt(scalarProd(dictB, dictB))
    cos = scalarProd(dictA, dictB) / ( lenA * lenB )
    return(cos)
    
    
