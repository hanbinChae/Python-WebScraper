import requests #url을 통해 웹 내용을 텍스트로 반환해주는 모듈
from bs4 import BeautifulSoup #원하는 HTML 파트 가져오기

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}";

def extract_indeed_page():
    result = requests.get(URL) #html 가져오기
    soup = BeautifulSoup(result.text, 'html.parser') #텍스트 전체를 html로 나누기
    pagination = soup.find('div',{'class':'pagination'}); #class 이름이 'pagination'인 div 찾아 변수에 저장
    links= pagination.find_all('a') #pagination 에서 링크 찾기
    pages = []
    for link in links[:-1]: #loop를 이용해 각 페이지의 <span> 모두 찾기
        pages.append(int(link.string))
    pages = pages[0:-1]
    max_page = pages[-1] 
    return max_page; #마지막 페이지 반환

def extract_indeed_jobs(last_page):
    jobs = []
#for page in range(last_page):
    result = requests.get(f"{URL}&start={0 * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "heading4"})
    for result in results:
        title = result.find("h2", {"class": "jobTitle"}).find("span", title=True).string
        print(title)
    return jobs