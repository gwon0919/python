import urllib.request as req
from bs4 import BeautifulSoup
import statistics  # 표준 편차를 계산하기 위해 statistics 모듈을 사용

print('BHC')

url = "https://www.bhc.co.kr/menu/best.asp"
data = req.urlopen(url)
soup = BeautifulSoup(data, 'html.parser')

menu_elements = soup.select("div.cont > h3")
price_elements = soup.select("strong > b")

#print(menu_elements)
#print(price_elements)

 # 메뉴 이름과 가격을 각각 리스트에 저장
menu_names = [menu.get_text(strip=True) for menu in menu_elements]
prices = [int(price.get_text(strip=True).replace(",", "")) for price in price_elements]
 
# # 메뉴 이름과 가격 출력
for menu_name, price in zip(menu_names, prices):
    print('메뉴이름: ', menu_name, ' 가격 :', price)
    
menu_count = len(menu_names)

# 총 가격 계산
total_price = sum(prices)

# 평균 가격 계산
average_price = sum(prices) / len(prices)

# 표준 편차 계산
std_dev = statistics.stdev(prices)

print("메뉴 개수: ", menu_count)
print("총 가격: ", total_price)
print("평균 가격: ", average_price)
print("표준 편차: ", std_dev)
