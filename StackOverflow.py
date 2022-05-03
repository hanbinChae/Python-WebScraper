import requests #url을 통해 웹 내용을 텍스트로 반환해주는 모듈
from bs4 import BeautifulSoup #원하는 HTML 파트 가져오기

KEY_WORD = 'python'
URL = f"https://stackoverflow.com/questions/tagged/{KEY_WORD}?tab=newest&page=2&pagesize=15";

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
    print(pages)
get_last_page()

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return []