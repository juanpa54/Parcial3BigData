from datetime import datetime
import requests 
import json
import boto3
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

year = datetime.today().strftime('%Y')
month = datetime.today().strftime('%m')
day = datetime.today().strftime('%d')

s3 = boto3.client('s3')

# Extracción análisis El Tiempo
directory_name = 'news/raw/periodico=eltiempo/year='+year+'/month='+month+'/day='+day 
url = 'https://www.eltiempo.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
urlsElTiempo = list()

for a in soup.find_all('a',class_='title page-link', href=True, text=True):
  urlsElTiempo.append(url+a['href'])

i=0

for url in urlsElTiempo:
  i=i+1
  r= requests.get(url)
  txt_data = r.text
  s3.put_object(Body=txt_data, Bucket='', Key=(directory_name+'/'+'noticia'+str(i)+'.txt'))

# Extracción análisis Publimetro
directory_name = 'news/raw/periodico=publimetro/year='+year+'/month='+month+'/day='+day 
url = 'https://www.publimetro.co/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
urlsPublimetro = list()

for a in soup.find_all('a', href=True, text=True, target="_self"):
  urlsPublimetro.append(url+a['href'])

i=0

for url in urlsPublimetro:
  i=i+1
  r= requests.get(url)
  txt_data = r.text
  s3.put_object(Body=txt_data, Bucket='', Key=(directory_name+'/'+'noticia'+str(i)+'.txt'))
