# HW3 - query part
import json
import os
import math
import utils
from collections import defaultdict
import heapq

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

term_ids = []
for term in query_stemmed_list:
    if voc.get(term) != None:
        term_ids.append(voc[term])
#term_ids = [voc[term] for term in query_stemmed_list]

if len(term_ids) == 0:
    print("Sorry, no results for the query.")
else:
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
        # print("Search engine 2 results: ", final)

        # construction of a dictionary representing the document vectors, obtained iterating on query terms
        # and on the set of result documents
        # Each entry of the dictionary (each document vector) is a dictionary itself, in which each entry
        # stores the term_id in the key, and the tfIdf in the value    
        docVectors = defaultdict(dict)
        for queryTermId in term_ids:
            for docId in final:            
                termFrequencies = idx[str(queryTermId)]
                for freq in termFrequencies:
                    if freq[0] == docId:                    
                        docVector = docVectors[docId]
                        docVector[queryTermId] = freq[1]
                        
        # print(docVectors)

        # construction of the query vector    
        parsed_dir = "C:\\Users\\nbonardo\\movies_parsed"
        n_files = len([name for name in os.listdir(parsed_dir) if os.path.isfile(os.path.join(parsed_dir, name))])
        queryVector = dict()
        nWordsQ = len(term_ids)
        for term_id in term_ids:                        
            term_idf = 1 + math.log(n_files / len(idx[str(term_id)]))        
            queryVector[term_id] = term_idf / nWordsQ
        #print("Query vector", queryVector)

        # calculation of the cosine similarity between each document vector of the result and the quere vector
        # storing the result (as tuple) in a heap structure
        h = []
        for doc in final:
            cos = utils.cosine(queryVector, docVectors[doc])
            #print("Cosine similarity of doc", doc, "=", cos, utils.getMovieTitle(doc))
            heapq.heappush(h, (cos, doc))

        # output of the top-K movies according to cosine similarity
        K = 5
        K = min(K, len(final))
        print("*** TOP-", K, " results ***")
        print(" Id  |        Title                             | Cosine Similarity")
        print("-----+------------------------------------------+------------------")
        for _ in range(K):
            movieTup = heapq.heappop(h)
            #print(movieTup[1], utils.getMovieTitle(movieTup[1]), movieTup[0])
            print("%4s | %40s | %.6s" % (movieTup[1]+1, utils.getMovieTitle(movieTup[1]), movieTup[0]))
        
    elif search_engine == '3':
        print("Sorry, search engine not implemented yet.")
    else:
        print("Sorry! You entered an incorrect value.")
        

