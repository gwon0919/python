#web scraping 연습
import  urllib.request as req
from bs4 import BeautifulSoup
import urllib

print('연습1 : 위키백과에서 검색된 자료 읽기----------')
url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
wiki = req.urlopen(url)
# print(wiki.read())
soup = BeautifulSoup(wiki, 'html.parser')
# print(soup)
print(soup.select("#mw-content-text > div.mw-parser-output > p"))
print()
result = soup.select("div.mw-parser-output > p > b")
print(result)

for s in result:
    print(s.string)
    
    
print('연습2 : 다음에서  뉴스 자료 읽기----------')
url = "https://news.daum.net/society#1" 
daum = req.urlopen(url)
soup = BeautifulSoup(daum, 'lxml')
data = soup.select_one("body > div.direct-link > a")
print(data)

datas = soup.select("body > div.direct-link > a")
print(datas)

for i in datas:
    href = i.attrs['href']
    text = i.string
    print('href:%s, text:%s'%(href,text))
    
print()
datas = soup.findAll('a')
#print(datas)
for i in datas:
    href = i.attrs['href']
    text = i.string
    #print('href:%s, text:%s'%(href,text))
    
print('연습3 : 네이버에서  시장지표 자료 중 미국 USD 읽기(일정 시간 마다 주기적으로 읽어 파일로 저장----------')
    
import datetime
import time

def workingFunc():
    url = "https://finance.naver.com/marketindex/"
    data = req.urlopen(url)
    soup = BeautifulSoup(data, 'lxml')
    price = soup.select_one("div.head_info > span.value").string
    # print('미국USD : ' , price)
    t = datetime.datetime.now()
    fname = "./usd/" + t.strftime('%Y-%m-%d-%H-%M-%S') + '.txt'
    
    with open(fname, mode ='w') as f:
        f.write(price)

while True:
    workingFunc()
    time.sleep(3)
        
    
# 메뉴명
#가격(,제외)
    
# 평균가격 표준편차
    
    
    
    
    
    
    
    
    
    
    
    
    