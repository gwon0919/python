# 위키백과 사이트에서 원하는 단어 문서 읽기 후 형태소 분석 - 단어 빈도 수 출력
import urllib
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from urllib import parse

para = "이순신"
para = parse.quote(para)    # 한글을 인코딩
url = "https://ko.wikipedia.org/wiki/" + para
print(url)              # https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0
page = urllib.request.urlopen(url).read().decode()
# print(page)
soup = BeautifulSoup(page,'html.parse')
# print(soup)

wordlist = []  # 형태소 분석으로 명사만 추출해 기억
okt = Okt()
for item in soup.select("#mw-content-text > div > p"):
    if item.string !=None:
        print(item.string)
        wordlist +=okt.nouns(item.string)
        
print('wordlist : ', wordlist)
print('단어 수 : ', len(wordlist))

word_dict = {}
for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
print('단어별 발생 횟수: ', word_dict)
print('발생 단어 수 : ', len(set(wordlist)))

import pandas as pd 

df = pd.DataFrame(wordlist, columns=['단어'])
print(df.head(3))

print()
df2 = pd.DataFrame([word_dict.keys(),word_dict.values()])
print(df2)
df2 = df2.T
df2.columns=['단어', '횟수']
print(df2.head(5))












