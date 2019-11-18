# Creation of the vocabulary file
import os
voc = dict()

parsed_dir = "movies_parsed"
n_parsed = len(os.listdir(parsed_dir))

for i in range(10000):
    try:        
        parsedFileName = parsed_dir + "\\article_" + str(i) + ".tsv"

        with open(parsedFileName, encoding="utf-8") as tsv_file:
            c = tsv_file.read()
        movie = c.split('\n')[1]
        movie_parts = movie.split('\t')        

        #building the vocabulary file
        for k in range(1,3):
            wordSet = movie_parts[k].split(' ')
            for word in wordSet:
                if word not in voc:
                    voc[word] = len(voc) + 1
    except:
        print("Error in file: ", i)

import json
with open("vocabulary.json", 'w', encoding="utf-8") as voc_file:
    js = json.dumps(voc)
    voc_file.write(js)
    
    
