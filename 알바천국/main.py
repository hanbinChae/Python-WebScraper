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

def get_jobs(html):
    #지역
    if html.find("td",class_="local first") == None:
        return 0;
    else:
        location = html.find("td",class_="local first").get_text()
        location = location.replace("\xa0","_")
    #
    
    return {"location":location}

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
            r = get_jobs(each_p)
            jobs.append(r)
    return jobs

testing = ['https://barogo.alba.co.kr/job/brand/main.asp']
pages = get_all_page(alba_url) #링크별 url 리스트
jobs_info = extract_info(testing) #직업별 정보들
print(jobs_info)

