# 1.3 Parse downloaded pages

import parser_utils
from bs4 import BeautifulSoup
import os

downloaded_dir = "movies_downloaded"
parsed_dir = "movies_parsed"

n_parsed = len(os.listdir(parsed_dir))
n_downloaded = len(os.listdir(downloaded_dir))
print("Movies already parsed: ", n_parsed)
print("Movies already downloaded: ", n_downloaded)

for i in range(0,10000):
    try:
        fileName = downloaded_dir + "\\article_" + str(i) + ".html"

        with open(fileName, encoding="utf-8") as html_file:
            soup = BeautifulSoup(html_file, 'lxml')

        title = soup.title.text            
        
        contentDiv = soup.find('div', class_="mw-parser-output")    

        # intro paragraph
        introP = contentDiv.select("p:not(.mw-empty-elt)")[0]
        intro = introP.text

        introP = introP.next_sibling
        while introP.name == 'None' or introP.name == 'p':        
            intro += introP.text
            introP = introP.next_sibling

        # finding h2 heading of plot section
        plotSpan = soup.select("span[id^=Plot]")[0]
        if plotSpan:                 
            next_p_tag = plotSpan.parent.findNext('p')
            plot = next_p_tag.text
            
            next_p_tag = next_p_tag.next_sibling        
            while next_p_tag.name == 'None' or next_p_tag.name == 'p':            
                plot += next_p_tag.text
                next_p_tag = next_p_tag.next_sibling            

        # preprocessing
        intro = parser_utils.preprocess(intro)
        plot = parser_utils.preprocess(plot)

        # writing output file - TSV format
        outputFileName = parsed_dir + "\\article_" + str(i) + ".tsv"

        with open(outputFileName, 'w', encoding="utf-8") as tsv_file:            
            title_line = "title \t intro \t plot \n"
            parsed_text = title + "\t" + intro + "\t" + plot
            tsv_file.write(title_line)
            tsv_file.write(parsed_text)
    except:
        print("Error in file ", i)
        with open("err/error_" + str(i) + ".ERR", 'w') as err_file:
            err_file.write("Error")



        



        
    
