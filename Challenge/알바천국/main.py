import requests
import csv
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

def convert_csv(jobs,html):
    if html.find("div",class_="keywordSearch") == None:
        title = '업체명 확인불가'
    elif html.find("div",class_="keywordSearch").find("a",class_="brandBtnType brandBtnArrow") == None:
        title = '업체명 확인불가'
    else:
        title = html.find("div",class_="keywordSearch").find("a",class_="brandBtnType brandBtnArrow").get_text()
    
    file = open(f"{title}.csv",mode ="w",encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(['Place', 'Title', 'Time', 'Payday','Pay','Date'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return

def extract_info(links):
    jobs = []
    idx=1
    for link in set(links):
        jobs = []
        print(f"{idx}/{len(links)}개 사이트 크롤링중...")      
        try:
            r = requests.get(link)
        except:
            continue;
        s = BeautifulSoup(r.text,"html.parser")
        p = s.find("div",id="NormalInfo").find_all("tr",class_="")
        idx+=1
        for each_p in p:
            r = get_info(each_p)
            jobs.append(r)
            convert_csv(jobs[1:],s)
    return jobs

pages = get_all_page(alba_url) #링크별 url 리스트
jobs_info = extract_info(pages) #직업별 정보들