# coding: utf-8
import requests
import requests
import time
import os
import sys
from bs4 import BeautifulSoup
import lxml
import csv
import json
# all categories 78

list_books=[]
imgs=[]
url = "https://www.pdfdrive.com/search"
page = 1
search = input("Entrer votre recherche ici : .....")
payload ={'q':search , 'pagecount':'', 'pubyear':'', 'searchin':'','em':'','page': page}
reponse = requests.get(url, params=payload )

if reponse.ok:

    html=reponse.text
    soup = BeautifulSoup( html,  "lxml")

    # find last page
    nav_page = soup.find( 'div', {'class':'Zebra_Pagination'})
    last_page = nav_page.find_all( 'a', { 'rel':'nofollow'})[-2].string
    
    # itere sur toutes les pages 
    for i in range(int(last_page)-1):

        livres = soup.find_all( 'div', {'class':'col-sm'}) # recupere tous les livres
        
        for livre in livres:
            img = livre.find('img', {'class', "img-zoom file-img"}).get('src')
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
            
            print(" |||+ img book :", img)
            print(" |||+ link livre :","https://www.pdfdrive.com" + link_livre)
            print(" |||+ page count : ",page_count)
            print(" |||+ year : ",year)
            print(" |||+ size : ",size)
            print(" |||+  number_down : ",number_down)
            print(" |||+ new : ",new)
            print(" -------------------------------------- -------------------------------------- --------------------------------------")
           
            book ={
                "img book": img,
                "link book": "https://www.pdfdrive.com" + link_livre,
                "page count":page_count,
                "year": year,
                "size":size,
                "number download":number_down,
                "new":new,
            }
            list_books.append(book)
            payload['page'] = i +1 # aller a la page suivant
            reponse = requests.get( url, params=payload)


with open("resultats.json","w",encoding='utf-8') as flux_json:
    json.dump(list_books,flux_json,indent=4)

with open('resultats.csv', mode='w') as csv_file:
    fieldnames = ['img book', 'link book', 'page count', 'year', 'size', 'number download', 'new']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for book_element in list_books:
       writer.writerow(book_element)

print(" |||+ nombre de resultats de votre recharche " + str(len(list_books)))
print("[+] Done")