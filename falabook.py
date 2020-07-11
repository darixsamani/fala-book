import requests
import requests
import time
import os
import sys
from bs4 import BeautifulSoup
import lxml
import csv

url = "https://www.pdfdrive.com" 


reponse = requests.get(url) 

if reponse.ok:
    soup = BeautifulSoup( reponse.text, "lxml")
    print(soup)