import requests
from bs4 import BeautifulSoup

alba_url = "http://www.alba.co.kr"

def get_all_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pages = soup.find("div",id="MainSuperBrand").find_all("a")
    RESULT = []
    for i in pages:
        RESULT.append(i['href'])
    return RESULT

def get_info(html):
    #지역
    if html.find("td",class_="local first") == None:
        place = ""
    else:
        place = html.find("td",class_="local first").get_text()
        place = place.replace("\xa0"," ")
    #회사명/공고제목
    if html.find("span",class_="title")==None:
        title = ""
    else:
        title = html.find("span",class_="title").string
    #시간
    if html.find("span",class_="time")==None:
        time = '시간 협의'
    else:
        time = html.find("span",class_="time").string
    #급여지급 방식
    if html.find("span",class_="payIcon day") == None:
        payday = "월급"
    else:
        payday = html.find("span",class_="payIcon day").string
    #급여
    if html.find("span",class_="number") == None:
        pay = ""
    else:
        pay = html.find("span",class_="number").string
    #등록일
    if html.find("td",class_="regDate last") == None: 
        date = ""
    else:
        date = html.find("td",class_="regDate last").string
    return {"place":place,"title":title,"time":time,"payday":payday,"pay":pay,"date":date}


def extract_info(links):
    jobs = []
    for link in set(links):
        try:
            r = requests.get(link)
        except:
            continue;
        s = BeautifulSoup(r.text,"html.parser")
        p = s.find("div",id="NormalInfo").find_all("tr",class_="")
        for each_p in p:
            r = get_info(each_p)
            jobs.append(r)
    return jobs

testing = ['https://barogo.alba.co.kr/job/brand/main.asp']
pages = get_all_page(alba_url) #링크별 url 리스트
jobs_info = extract_info(pages) #직업별 정보들
print(jobs_info)
print(len(jobs_info),'개')
