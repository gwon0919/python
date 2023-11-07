# [one-sample t 검정 : 문제1]  
# 영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다. 
# 한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간 관련 자료를 얻었다. 
# 한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas.io.excel._base import read_excel

# 귀무 : 영사기에 사용되는 신형 백열전구의 수명은 300시간이다.
# 대립 : 영사기에 사용되는 신형 백열전구의 수명은 300시간이 아니다.

one_sample = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
print(np.array(one_sample).mean())                 # 289
print('정규성 확인 : ', stats.shapiro(one_sample))   # pvalue=0.820 > 0.05 정규성 만족 
result = stats.ttest_1samp(one_sample, popmean=289)
print(result)       # TtestResult(statistic=0.11972581985977475, pvalue=0.9065308269755065, df=13)
print('statistic(t값):%.5f, pvalue:%.5f'%result) # statistic(t값):0.11973, pvalue:0.90653
# 해석 : pvalue:0.90 > 0.05 이므로 귀무 채택.

print('-------------------------------')
# [one-sample t 검정 : 문제2] 
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. 
# A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", "")

# 귀무 : A회사에서 생산된 노트북 평균시간과 국내에서 생산된 대다수의 노트북 평균 사용 시간이 차이가 있다.
# 대립 : A회사에서 생산된 노트북 평균시간과 국내에서 생산된 대다수의 노트북 평균 사용 시간이 차이가 없다.
data = pd.read_csv("../testdata/one_sample.csv")
data['time'] = pd.to_numeric(data['time'].replace("     ", ""), errors='coerce')
data = data.dropna()
print(data.head(10), len(data)) # 150
#print(data.describe())
print(np.mean(data.time)) # 5.5

result2 = stats.ttest_1samp(data.time, popmean=5.5)
print(result2)      # TtestResult(statistic=0.6289349437842267, pvalue=0.5307196667712607, df=108)
print('statistic(t값):%.5f, pvalue:%.5f'%result2)
# 해석 : pvalue:0.53 > 0.05 이므로 귀무 채택.

print('--------------------------------')
# [one-sample t 검정 : 문제3] 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오.

# 귀무 : 전국 평균 미용 요금이 15000원이다.
# 대립 : 전국 평균 미용 요금이 15000원이 아니다.

data2 = pd.read_excel("../testdata/service_loc.xls")
data2 = data2.dropna(axis=1)
data2 = data2.drop(['번호','품목'], axis=1)
print(data2.T)
print(np.mean(data2.T.iloc[:,0]))       # 18311.875

result3 = stats.ttest_1samp(data2.iloc[0], popmean=15000)
print(result3)      # TtestResult(statistic=6.285993008166382, pvalue=1.4593857848302074e-05, df=15)
print('statistic(t값):%.5f, pvalue:%.5f'%result3)
# 해석 : pvalue:0.00001 < 0.05이므로 귀무 기각



















