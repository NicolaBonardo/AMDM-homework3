# AMDM - Homework 3 - Group #36 (Nicola Bonardo)

This repository contains the files for HW3:
* README.md - this markdown itself
* Main.ipynb - a Jupyter notebook with explanations about choices made
* collector.py - the code to parse the html file with the list of movies and to crawl Wikipedia to download them
* parser.py and parser_utils.py - the code to parse the downloaded html files, and to produce corresponding .tsv files
* vocabulary.py - the code to create a vocabulary.json file with all the terms found in the documents
* index.py - the code to create a simple inverted index (index.json) and a more sophisticated term frequency - inverted document frequency index (tfIdfIndex.json)
* main.py - the code to launch the search engine
* utils.py - a helper code file, with common methods
* exercise_4.py - the code for the theoretical exercise
* images - a folder with some screenshots cited in the Jupyter notebook
* usual gitignore and license files

Please notice:
* unfortunately customized search engine was not implemented, nor the addition info from infobox was retrieved, due to lack of time
* I decided not to use libraries for vectorialization of documents, because I thought it was better from a learning point of view
* My cosine similarity seems working in the opposite way, and the best matches are with lower cosine. I would like to analyze why, in the meantime I leave the top-k ranking in ascending order.
