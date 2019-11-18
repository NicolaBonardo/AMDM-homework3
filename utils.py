# Utilities
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer

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
    
    
