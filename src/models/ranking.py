from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
driver = webdriver.Chrome('.chromedriver')  # 드라이버를 실행합니다.


url = "https://search.kyobobook.co.kr/web/search?vPstrKeyWord=%25EB%25B9%2584%25EC%25A0%2584%25EA%25B3%25B5%25EC%259E%2590&searchPcondition=1&searchCategory=%EA%B5%AD%EB%82%B4%EB%8F%84%EC%84%9C@KORBOOK@@%EC%BB%B4%ED%93%A8%ED%84%B0/IT@33&collName=KORBOOK&from_CollName=%EC%A0%84%EC%B2%B4@UNION&vPstrTab=PRODUCT&from_coll=KORBOOK&row=60&currentPage=1&orderClick=LIZ"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url, headers=headers)

driver.get(url)  # 드라이버에 해당 url의 웹페이지를 띄웁니다.
sleep(5)  # 페이지가 로딩되는 동안 5초 간 기다립니다.

req = driver.page_source  # html 정보를 가져옵니다.
driver.quit()  # 정보를 가져왔으므로 드라이버는 꺼줍니다.

# soup = BeautifulSoup(data.text, 'html.parser')
soup = BeautifulSoup(req, 'html.parser')  # 가져온 정보를 beautifulsoup으로 파싱해줍니다.

books = soup.select("#search_list > tr")

for book in books:
                title = book.select_one("td.detail > div.title > a > strong").text.strip()
                image = book.select_one("td.image > div.cover > a > img")['src']
                author = book.select_one("td.detail > div.author > a:nth-child(1)").text.strip()
                url = book.select_one("td.detail > div.title > a")['href']

                doc = { 'title' : title,
                        'image' : image,
                        'author' : author,
                        'url' : url,

                }
                db.books.insert_one(doc)
