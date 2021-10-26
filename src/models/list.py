from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from pymongo import MongoClient

client = MongoClient()
db = client.dbsparta


driver = webdriver.Chrome('/Users/cleanwater/Desktop/sparta/project_awsomebooks/chromedriver')

url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=437"

driver.get(url)
sleep(3)

req = driver.page_source
driver.quit()


soup = BeautifulSoup(req, 'html.parser')
books = soup.select('#Myform > div')

for book in books :
    a_tag = book.select_one('table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td > div')
    if a_tag is not None:
        rank = a_tag.text

    b_tag = book.select_one('table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a:nth-child(1)')
    if b_tag is not None:
        author = b_tag.text

    bb_tag = book.select_one('table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(3) > a:nth-child(1)')
    if bb_tag is not None:
        author = bb_tag.text

    c_tag = book.select_one('table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li')
    if c_tag is not None:
        title = book.select_one(' a > b').text

    d_tag = book.select_one('table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > div:nth-child(2) > a > img')
    if d_tag is not None:
        image = d_tag

        doc = {
            'rank': rank,
            'author': author,
            'title': title,
            'image': image,
        }
        db.books.insert_one(doc)








