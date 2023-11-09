# 일원 분산 분석 검정
# 어느 음식점의 매출 데이터와 날씨 데이터, 두 개의 파일을 이용해 최고 기온에 따른 음식점 매출액 평균의 차이를 검정
# 귀무 : 기온에 따른 음식점 매출액 평균의 차이는 없다.
# 대립 : 기온에 따른 음식점 매출액 평균의 차이는 있다.

import numpy as np
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt

# 매출 데이터
sales_data = pd.read_csv("../testdata/tsales.csv", dtype={'YMD':'object'})
print(sales_data.head(3))       # YMD : 20190514
print(sales_data.info())

# 날씨 데이터
wt_data = pd.read_csv("../testdata/tweather.csv")
print(wt_data.head(3))          # tm : 2018-06-01
print(wt_data.info())
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-',''))
print(wt_data.head(3))          # tm : 20180601

# merge
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')
print(frame.head(3))
print(frame.tail(3), frame.shape)
print(frame.columns)    # 'YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs', 'ddMes'

data = frame.iloc[:,[0,1,7,8]]      #  YMD(날짜)    AMT(매출액)  maxTa(최고기온)  sumRn(강수량)
print(data.head(3))
print(data.isnull().sum())
print(data.maxTa.describe())
# count    328.000000
# mean      18.597866
# std       10.163039
# min       -4.900000
# max       36.800000

# plt.boxplot(data.maxTa)
# plt.show()

# 온도를 임의로 추움, 보통, 더움 (0,1,2) 세 구간으로 나눠 그룹을 형성 
data['Ta_gubun']=pd.cut(data.maxTa, bins=[-5, 8, 24, 37], labels=[0, 1, 2])
print(data.head(3))

print(data.corr())      # 상관계수로 관계 확인

# 세 그룹으로 데이터 분리 : 등분산성, 정규성 만족 여부 확인 - 종속변수가 해당
x1 = np.array(data[data.Ta_gubun == 0].AMT)
x2 = np.array(data[data.Ta_gubun == 1].AMT)
x3 = np.array(data[data.Ta_gubun == 2].AMT)
print(x1[:10], len(x1))                 # len 69
print(x2[:10])
print(x3[:10])

# 등분산성
print(stats.levene(x1,x2,x3).pvalue)        # 0.03900 < 0.05 등분산성을 따르지 못했다.

# 정규성
print(stats.ks_2samp(x1,x2).pvalue, stats.ks_2samp(x1,x3).pvalue, stats.ks_2samp(x2,x3).pvalue) # 정규성 x

# 온도별 매출액 평균
tempAmt = data.loc[:, ['AMT', 'Ta_gubun']]
print(tempAmt.groupby('Ta_gubun').mean())

print(pd.pivot_table(tempAmt, index=['Ta_gubun'], aggfunc='mean'))
 
tempAmtArr = np.array(tempAmt)
# print(tempAmtArr)       # [      0       2] [  18000       1]
group1 = tempAmtArr[tempAmtArr[:, 1] == 0, 0]
group2 = tempAmtArr[tempAmtArr[:, 1] == 1, 0]
group3 = tempAmtArr[tempAmtArr[:, 1] == 2, 0]

# plt.boxplot([group1, group2, group3], meanline=True, showmeans=True)
# plt.show()

print()
print('\n-----------------one way anova--------------------')
print(stats.f_oneway(group1, group2, group3))       # statistic=99.1908012029983, pvalue=2.360737101089604e-34
# pvalue=2.360737101089604e-34 < 0.05이므로 귀무가설 기각.

print('정규성을 만족하지 않았으므로 Kruskal-Walis test')
print(stats.kruskal(group1, group2, group3))          # pvalue=1.5278142583114522e-29

print('등분산성을 만족하지 않았으므로 welch_anova')
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(data=data, dv='AMT', between='Ta_gubun')) # p-unc =7.907874e-35 < 0.05

# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
postHoc = pairwise_tukeyhsd(tempAmt['AMT'], tempAmt['Ta_gubun'], alpha=0.05)
print(postHoc)

postHoc.plot_simultaneous()
# plt.show()

# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하지 않는다.
# 대립 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재한다.

kind = [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2]
quantity = [64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]

# 데이터프레임 생성
df = pd.DataFrame({'kind': kind, 'quantity': quantity})

# NaN 값을 해당 칼럼의 평균 값으로 대체
mean_quantity = df['quantity'].mean()
df['quantity'].fillna(mean_quantity, inplace=True)
print(df)

result = df[['kind', 'quantity']]
m1 = result[result['kind'] == 1]
m2 = result[result['kind'] == 2]
m3 = result[result['kind'] == 3]
m4 = result[result['kind'] == 4]

gr1 = m1['quantity']
gr2 = m2['quantity']
gr3 = m3['quantity']
gr4 = m4['quantity']

print(gr1[:3])
print(gr2[:3])
print(gr3[:3])
print(gr4[:3])

oilAmt = df.loc[:, ['kind','quantity']]
print(pd.pivot_table(oilAmt, index=['kind'], aggfunc='mean'))
 
oilAmtArr = np.array(oilAmt)

print(stats.f_oneway(gr1, gr2, gr3, gr4))   # statistic=0.26693511759829797, pvalue=0.8482436666841788
# pvalue=0.84 > 0.05 

oilTk = pairwise_tukeyhsd(oilAmt['quantity'], oilAmt['kind'], alpha=0.05)
print(oilTk)

oilTk.plot_simultaneous()
plt.show()


# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오. 
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.





