import requests #url을 통해 웹 내용을 텍스트로 반환해주는 모듈
from bs4 import BeautifulSoup #원하는 HTML 파트 가져오기
#새로운 강의 수강하면서 수정
LIMIT = 10;
KEY_WORD = 'python'
URL = f"https://stackoverflow.com/questions/tagged/{KEY_WORD}?tab=newest&page=2&pagesize=15";

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
    last_page = LIMIT#임의로 100으로 설정함.
    return int(last_page)

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"s-post-summary"})
        for result in results:
            print(result.find("a",{"class":"s-link"}).string)

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return []

get_jobs()