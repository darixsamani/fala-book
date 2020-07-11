# coding: utf-8
import requests
import requests
import time
import os
import sys
from bs4 import BeautifulSoup
import lxml
import csv

# all categories 78

url = "https://www.pdfdrive.com/search"

payload ={'q':'java' , 'pagecount':'', 'pubyear':'', 'searchin':'','em':'','page':'1'}
reponse = requests.get(url, params=payload ) 

if reponse.ok:
    html=reponse.text
    soup = BeautifulSoup( html,  "lxml")

    livres = soup.find_all( 'div', {'class':'file-right'}) # recupere tous les libres
    for livre in livres:
        link_livre = livre.find('a').get('href')
        try:
            page_count = livre.find( 'span', {'class', 'fi-pagecount'}).get_text()
        except:
            page_count = "inconnu"
        
        year = livre.find( 'span', { 'class', 'fi-year'}).get_text()
        size = livre.find( 'span', { 'class', 'fi-size hidemobile'}).get_text()
        number_down = livre.find( 'span', { 'class', 'fi-hit'}).get_text()
        try:
            new = livre.find( 'span', {'class', 'new'} ).get_text()
        except:
            new = "old"
        

        print(" |||+ link livre :",link_livre)
        print(" |||+ page count : ",page_count)
        print(" |||+ year : ",year)
        print(" |||+ size : ",size)
        print(" |||+  number_down : ",number_down)
        print(" |||+ new : ",new)
        print(" --------------------------------------")

