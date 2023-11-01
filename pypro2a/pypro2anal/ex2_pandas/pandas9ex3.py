import urllib.request as req
from bs4 import BeautifulSoup
import statistics  

print('공차')

url = "https://www.gong-cha.co.kr/brand/menu/product.php?c=001002"
data = req.urlopen(url)
soup = BeautifulSoup(data, 'html.parser')

menu_elements = soup.select("a > span.txt")
price_elements = soup.select("div.price > span.cost")

#productView > div > div.info > div.hgroup > div > p.box.s2 > span.cost

print(menu_elements)
print(price_elements)

#===============================================================================
# # 메뉴 이름과 가격을 각각 리스트에 저장
# menu_names = [menu.get_text(strip=True) for menu in menu_elements]
# prices = [int(price.get_text(strip=True).replace(",", "")) if price.get_text(strip=True).isdigit() else 0 for price in price_elements]
# menu_count = len(menu_names)
# 
# # 메뉴 이름과 가격을 출력
# for menu, price in zip(menu_elements, price_elements):
#     menu_name = menu.get_text(strip=True)
#     price_text = price.get_text(strip=True)
#     print('메뉴이름:', menu_name, '가격:', price_text)
# 
# 
# # 총 가격 계산
# total_price = sum(prices)
# 
# # 평균 가격 계산
# average_price = total_price / menu_count if menu_count > 0 else 0
# 
# # 표준 편차 계산
# std_dev = statistics.stdev(prices) if menu_count > 1 else 0
# 
# print("메뉴 개수: ", menu_count)
# print("총 가격: ", total_price)
# print("평균 가격: ", average_price)
# print("표준 편차: ", std_dev)
#===============================================================================
