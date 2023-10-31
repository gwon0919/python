# https://www.kma.go.kr/XML/weather/sfc_web_map.xml
# 기상청 제공 국내 주요 지역 날씨 정보 XML문서 읽기
import urllib.request
import xml.etree.ElementTree as etree

# 웹 문서를 읽어 파일로 저장 후 XML문서 처리
try:
    webdata = urllib.request.urlopen("https://www.kma.go.kr/XML/weather/sfc_web_map.xml")
    print(webdata)      # HTTPResponse object 
    webxml = webdata.read()
    webxml = webxml.decode('utf-8')
#    print(webxml)
    webdata.close()
    with open('pandas6.xml', mode='w', encoding="utf-8") as obj:
        obj.write(webxml)
    print("sucess")
except Exception as e:
    print('err : ', e)
    
xmlfile = etree.parse("pandas6.xml")
print((xmlfile))            # xml.etree.ElementTree
root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)       # {current}weather

children =  root.findall('{current}weather')
print(children) #Element

for it in children:
    y = it.get('year')  # 속성 값 읽기
    m = it.get('month')
    d = it.get('day')
    h = it.get('hour')
    print(y + "년 "  + m + "월 " + d + "일" + h + "시 현재 날씨 정보")
    
datas=[]
for child in root:
#    print(child.tag) # weather
    for it in child:
       # print(it.tag)
        localName = it.text     # 지역명
        re_ta = it.get("ta")
        re_desc = it.get("desc")
        #print(localName, re_ta, re_desc)
    datas += [[localName, re_ta, re_desc]]
#print(datas)  #[['속초', '20.7', '맑음'], ['북춘천', '19.8', '맑음'],..

import pandas as pd
import numpy as np

df = pd.DataFrame(datas, columns=['지역', '온도', '상태'])
print(df.head(3))
print(df.tail(3))

imsi = np.array(df.온도, np.float32)
#imsi= list(map(float, imsi))

print(imsi)
print('평균온도 : ', np.mean(imsi))







