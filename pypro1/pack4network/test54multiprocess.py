# 멀티 프로세싱을  통한 웹 스크랩핑
import requests
from bs4 import BeautifulSoup as bs
import time 
from multiprocessing import Pool
from conda.core import link

# 스크래핑 대상 컨텐츠
# https://beomi.github.io/beomi.github.io_old/ 
def get_links():
    data = requests.get("https://beomi.github.io/beomi.github.io_old/").text
    soup = bs(data, 'html.parser')
    print(type(data))
    my_titles = soup.select('h3 > a')
    data = []
    
    for title in my_titles:
        data.append(title.get('href'))
    return data

def get_content(link):
    abs_link = "https://beomi.github.io" + link
    #print(abs_link)
    data = requests.get(abs_link).text
    print(data)
    #soup = bs(data,'html.parser')
    #print(soup.select('h1')[0].text)
    
   
if __name__ == '__main__':
   # print(get_links())
    #print(len(get_links()))
    start_time = time.time()
    '''
    for link in get_links():
        get_content(link)
    '''
    pool = Pool(processes = 4)
    pool.map(get_content, get_links())
    
    print("---%s 초---"%(time.time()- start_time))       
    # 직렬: 9.577519655227661 초
    # 병렬: 4.340705156326294 초
    # robots.txt
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    