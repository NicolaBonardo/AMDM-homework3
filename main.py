# HW3 - query part
import json
import os
import math
import utils

print('''## AMDM-2019 ##
WHAT MOVIE TO WATCH TONIGHT?

There are 3 search engines available:
1 - A simple Inverted Index search engine
2 - tfIdf Inverted Index search engine
3 - A custom search engine''')

search_engine = input("Please choose the Search Engine: ")
query = input("Please insert a query:")

# stemming query terms, to match vocabulary
query_stemmed_list = utils.stemList(query.split(' '))

# loading vocabulary
with open("vocabulary.json", encoding="utf-8") as voc_file:     
    voc = dict(json.load(voc_file))

term_ids = [voc[term] for term in query_stemmed_list]
#print(term_ids)

if search_engine == '1':    
    #loading simple inverted index
    with open("index.json", encoding="utf-8") as idx_file:
        js_idx = json.load(idx_file)
        idx = dict(js_idx)
    resultMovies = []
    for term_id in term_ids:
        moviesList = idx[str(term_id)]        
        uniqueMoviesList = set(moviesList)
        resultMovies.append(uniqueMoviesList) 
    final = set.intersection(*resultMovies)    
    print("Search engine 1 results: ")
    for movie in final:
        print(utils.getMovieTitle(movie))

elif search_engine == '2':
    #loading tfIdf inverted index
    with open("tfIdfIndex.json", encoding="utf-8") as idx_file:
        js_idx = json.load(idx_file)
        idx = dict(js_idx)
    resultMovies = []
    for term_id in term_ids:
        moviesList = idx[str(term_id)]
        uniqueMoviesList = set()
        for movie in moviesList:
            uniqueMoviesList.add(movie[0])
        resultMovies.append(uniqueMoviesList)    
    final = set.intersection(*resultMovies)    
    print("Search engine 2 results: ", final)
    # Fin qui ho ottenuto un insieme di id di film
    
    # 1 costruisco il vettore per la query. Avrà tante componenti quante sono le parole della query esistenti nel vocabolario
    # per ciascuna, calcolo il idf e faccio la media
    parsed_dir = "C:\\Users\\nbonardo\\movies_parsed"
    n_files = len([name for name in os.listdir(parsed_dir) if os.path.isfile(os.path.join(parsed_dir, name))])
    query_vector = []
    nWordsQ = len(term_ids)
    for term_id in term_ids:
        #print(term_id)                
        term_idf = 1 + math.log(n_files / len(idx[str(term_id)]))
        #print(term_idf)
        query_vector.append((term_id, term_idf / nWordsQ))
    print("Query vector", query_vector)    
    
elif search_engine == '3':
    print("Sorry, search engine not implemented yet.")
else:
    print("Sorry! You entered an incorrect value.")
    

