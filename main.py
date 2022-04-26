import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
#print(indeed_result.text); #html 가져오기

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find('div',{'class':'pagination'});

pages= pagination.find_all('a')
spans = []
for page in pages:
    spans.append(page.find('span'))

spans = spans[0:-1]