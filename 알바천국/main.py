from __future__ import print_function
from multiprocessing import connection
import requests
from bs4 import BeautifulSoup

alba_url = "http://www.alba.co.kr"

def get_last_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pages = soup.find("div",id="MainSuperBrand").find_all("a")
    RESULT = []
    for i in pages:
        RESULT.append(i['href'])
    return RESULT

def convert_excel(links):
    for link in set(links):
        try:
            r = requests.get(link)
        except:
            continue;
        s = BeautifulSoup(r.text,"html.parser")
        p = s.find("div",id="NormalInfo").find("td",class_="local first ")
        print(p)

pages = get_last_page(alba_url) #링크별 url 리스트
convert_excel(pages);

