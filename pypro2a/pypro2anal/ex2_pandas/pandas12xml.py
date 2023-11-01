# XML 문서 읽기 : 서울시 제공 도서관 정보 5개 읽기
import urllib.request as req
from bs4 import BeautifulSoup

url = "https://raw.githubusercontent.com/pykwon/python/master/seoullibtime5.xml"
plainText = req.urlopen(url).read().decode()
#print(plainText)

xmlObj = BeautifulSoup(plainText, 'lxml')
libData = xmlObj.select('row')
#print(libData)        # lbrry_name  adres

for d in libData:
    name = d.find('lbrry_name').text        # text or string
    addr = d.find('adres').string
    print('도서관명 : ', name)
    print('주소 :  ', addr + "\n")
    
 
