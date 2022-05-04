import requests #url을 통해 웹 내용을 텍스트로 반환해주는 모듈
from bs4 import BeautifulSoup #원하는 HTML 파트 가져오기

KEY_WORD = 'python'
URL = f"https://stackoverflow.com/jobs/companies?q={KEY_WORD}";
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

def extract_job(html):
    title = html.find("h2").find("a",{"class":"s-link"}).get_text()
    location,company = html.find("div",{"class":"fs-body1"}).find_all("div",recursive=False)
    location = location.get_text()
    company = company.get_text()
    job_id = html.find("h2").find("a",{"class":"s-link"})["href"]
    job_id = "https://stackoverflow.com/"+job_id
    return {"title":title,"location":location,"company":company,"job_id":job_id}
    

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping StackOverflow page : {page+1}")
        result = requests.get(f"{URL}&pg={int(page)+1}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"flex--item fl1 text mb0"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs