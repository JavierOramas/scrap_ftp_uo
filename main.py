import requests
from bs4 import BeautifulSoup
import os
import path

url = 'http://ftp.uo.edu.cu/Programacion/Flutter%20Dise%C3%B1os%20nivel%20profesionales%20y%20animaciones/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
payload = {
    'query':'test'
}

response = requests.get(url, data=payload, headers=headers)
soup = BeautifulSoup(response.text,'html.parser')

links = soup.find_all('a')

index = 1
for i in links:
    if i['href'].startswith('/Programacion'):
        response = requests.get('http://ftp.uo.edu.cu'+i['href'])
        soup = BeautifulSoup(response.text,'html.parser')
        items = soup.find_all('a')
        for j in items:
            if index < 11:
                break
            if j['href'].startswith('/Programacion'):
                link = "http://ftp.uo.edu.cu"+j["href"]
                os.system(f'wget {link} -P {index}')
        index += 1
        