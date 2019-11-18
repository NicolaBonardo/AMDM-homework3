# Homework 3 - What movie to watch tonight?

from bs4 import BeautifulSoup
import requests
import time
import os
from random import seed
from random import random

# Parsing the html page and getting the complete list of urls
with open('movies1.html') as movies_file:
    soup = BeautifulSoup(movies_file, 'lxml')

movies = [link['href'] for link in soup.find_all('a')]
    
# Crawling Wikipedia
# seeding the random numbers generator
seed(37)

movies_dir = "movies"

n_movies_downloaded = len(os.listdir(movies_dir))
print("Movies already downloaded: ", n_movies_downloaded)

for url in movies[n_movies_downloaded:]:    
    
    print("Requesting url: ", url)
    try:
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            print("Status", r.status_code, " - Request OK")            
            fileName = movies_dir + "/article_" + str(n_movies_downloaded) + ".html"
            with open(fileName, 'w', encoding="utf-8") as wf:                
                wf.write(r.text)
            n_movies_downloaded += 1
            
            # wait a random time between 1 and 5 seconds before the next request
            sleepTime = 1 + 4 * random()
            print("Waiting ", sleepTime, " seconds")
            time.sleep(sleepTime)
        elif r.status_code == 404:
            print("Status", r.status_code, " - Page not found")
            fileName = movies_dir + "/article_" + str(n_movies_downloaded) + ".html_FILE_NOT_FOUND"
            with open(fileName, 'w', encoding="utf-8") as wf:                
                wf.write("")
            n_movies_downloaded += 1
            
            # wait a random time between 1 and 5 seconds before the next request
            sleepTime = 1 + 4 * random()
            print("Waiting ", sleepTime, " seconds")
            time.sleep(sleepTime)            
        else:
            print("Status", r.status_code)
            break
        
    except Exception as e:
        print("Exception during retrieval of url: ", url)
        print(e)
    


