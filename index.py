import json
from collections import Counter
from collections import defaultdict
import os
import math
 
#loading of the vocabulary
with open("vocabulary.json", encoding="utf-8") as voc_file:
    js = json.load(voc_file)
    voc = dict(js)

parsed_dir = "movies_parsed"

# Creation of the inverted index for Query #1
idx = defaultdict(list)

for i in range(0, 10000):
    try:
        parsedFileName = parsed_dir + "\\article_" + str(i) + ".tsv"
        
        with open(parsedFileName, encoding="utf-8") as tsv_file:
            c = tsv_file.read()
            movie = c.split('\n')[1]
            movie_parts = movie.split('\t')

            for k in range(1,3):
                wordSet = movie_parts[k].split(' ')
                for word in wordSet:
                    term_id = voc[word]            
                    idx[term_id].append(i)
    except:
        print("Error in file", i)                    

import json
with open("index.json", 'w', encoding="utf-8") as idx_file:
    js = json.dumps(idx)
    idx_file.write(js)

# Construction of the Tf-Idf (term frequency - inverted document frequency) index
n_files = len([name for name in os.listdir(parsed_dir) if os.path.isfile(os.path.join(parsed_dir, name))])

# step1 - construction of an inverted index with ONLY normalized frequency
tfIndex = defaultdict(list)

for i in range(0, 10000):
    try:        
        parsedFileName = parsed_dir + "\\article_" + str(i) + ".tsv"
        
        with open(parsedFileName, encoding="utf-8") as tsv_file:
            c = tsv_file.read()            
            movie = c.split('\n')[1]
            movie_parts = movie.split('\t')
            # I consider intro and plot as part of the same document
            doc = movie_parts[1] + ' ' + movie_parts[2]
            words = doc.split(' ')
            #for each document, I create a counter
            counter = Counter(words)            
            n_words = sum(counter.values())            

            # for each word in the counter, I append to the index a tuple with termId and termFrequency
            for word in counter:                
                tup = (i, counter[word]/n_words)
                term_id = voc[word]   
                tfIndex[term_id].append(tup)
                
    except Exception as e:
        print("Exception in file: ", i)
        print(e)

# construction of an inverted index with term frequency * idf
tfIdfIndex = defaultdict(list)

for j in tfIndex:
    # for each term in the tfIndex, I calculate the Inverse Document Frequency
    idf = 1 + math.log(n_files / len(tfIndex[j]))    
    # print("Term", j, " - Occurrencies", len(tfIndex[j]), " - Idf", idf, tfIndex[j])
    for tup in tfIndex[j]:
        # for each tuple in the j-th term, I create a new tuple (termId, tf * idx) and append it to new index
        newTup = (tup[0], tup[1] * idf)
        tfIdfIndex[j].append(newTup) 

# Saving the index created
with open("tfIdfIndex.json", 'w', encoding="utf-8") as tfIdfIdx_file:
    js = json.dumps(tfIdfIndex)
    tfIdfIdx_file.write(js)
        

    
