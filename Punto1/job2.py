from datetime import datetime
import requests 
import json
import boto3
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


s3 = boto3.client('s3')

# Analisis El Tiempo

url = 'https://www.eltiempo.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
noticias = [list(),list(),list()]

for a in soup.find_all('a',class_='title page-link', href=True, text=True):
  seccion = ""
  slashEncontrado = 0
  # Ciclo para extraer la sección del href
  for char in a['href']:
    if char == '/':
      slashEncontrado = slashEncontrado+1
    if slashEncontrado == 1:
      seccion = seccion+char
  etiqueta = a.text
  title = etiqueta.replace(',',"")
  noticias[0].append(title)
  noticias[1].append(seccion[1:])
  noticias[2].append(url+a['href'])

print(noticias)
df = pd.DataFrame(noticias).transpose()


year = datetime.today().strftime('%Y')
month = datetime.today().strftime('%m')
day = datetime.today().strftime('%d')
directory_name = 'headlines/final/periodico=eltiempo/year='+year+'/month='+month+'/day='+day 
df.to_csv('s3://news043parcial3/'+directory_name+'/'+'Analisis_El_tiempo.csv', index=False)

# Analisis Publimetro

url = 'https://www.publimetro.co/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
noticias = [list(),list(),list()]

for a in soup.find_all('a', href=True, text=True, target="_self"):
  seccion = ""
  slashEncontrado = 0
  # Ciclo para extraer la sección del href
  for char in a['href']:
    if char == '/':
      slashEncontrado = slashEncontrado+1
    if slashEncontrado == 1:
      seccion = seccion+char
  etiqueta = a.text
  title = etiqueta.replace(',',"")
  noticias[0].append(title)
  noticias[1].append(seccion[1:])
  noticias[2].append(url+a['href'])

print(noticias)
df = pd.DataFrame(noticias).transpose()


year = datetime.today().strftime('%Y')
month = datetime.today().strftime('%m')
day = datetime.today().strftime('%d')
directory_name = 'headlines/final/periodico=publimetro/year='+year+'/month='+month+'/day='+day 
df.to_csv('s3://news043parcial3/'+directory_name+'/'+'Analisis_Publimetro.csv', index=False)