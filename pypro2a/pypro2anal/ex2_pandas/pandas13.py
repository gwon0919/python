# 기상청 제공 중기 예보 웹 문서 읽기
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url="https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data = urllib.request.urlopen(url).read()
# print(data)

soup = BeautifulSoup(data,'lxml')
title = soup.find('title').text
print(title)
# wf = soup.find('wf')
# print(wf.text)

city = soup.find_all('city')
# print(city)
cityDatas = []
for c in city:
    cityDatas.append(c.string)

df = pd.DataFrame()
df['city'] = cityDatas
# print(df)

tempMins = soup.select('location > province + city + data > tmn' )     # + : next silbling, - :previous silbling
# print(tempMins)
tempDatas =[]
for t in tempMins:
    tempDatas.append(t.string)
    
df['temp_m'] = tempDatas
df.columns = ['지역', '최저온도']
print(df)


# ... 
