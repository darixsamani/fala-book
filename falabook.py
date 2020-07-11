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
page = 1
payload ={'q':'java' , 'pagecount':'', 'pubyear':'', 'searchin':'','em':'','page': page}
reponse = requests.get(url, params=payload ) 

if reponse.ok:

    html=reponse.text
    soup = BeautifulSoup( html,  "lxml")

    # find last page
    nav_page = soup.find( 'div', {'class':'Zebra_Pagination'})
    last_page = nav_page.find_all( 'a', { 'rel':'nofollow'})[-2].string
    
    # itere sur toutes les pages 
    for i in range(int(last_page)-1):

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
            payload['page'] = i +1 
            reponse = requests.get( url, params=payload)
