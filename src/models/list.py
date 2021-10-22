from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Chrome('/Users/cleanwater/Desktop/sparta/project_awsomebooks/chromedriver')

url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=437"

driver.get(url)

req = driver.page_source
driver.quit()
sleep(3)

soup = BeautifulSoup(req, 'html.parser')

divs = soup.select('#Myform > div')

for div in divs :
    a_tag = div.select_one('table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(1) > td > div')
    if a_tag is not None:
        rank = a_tag.text

    b_tag = div.select_one('table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a:nth-child(1)')
    if b_tag is not None:
        author = b_tag.text

    bb_tag = div.select_one('table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(3) > a:nth-child(1)')
    if bb_tag is not None:
        author = bb_tag.text

    c_tag = div.select_one('table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li')
    if c_tag is not None:
       title = div.select_one(' a > b').text

    d_tag = div.select_one('table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > div:nth-child(2) > a > img')
    if d_tag is not None:
        image = d_tag

        print(rank,author,title)
        print(image)








