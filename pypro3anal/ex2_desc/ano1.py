# 세개 이상의 모집단에 대한 가설검정 - 분산분석
# ‘분산분석' 이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고 요인
# 에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.
# 세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제 1 종 오류가 증가하게 되어 문제가 발생한다
# 이를 해결하기 위해 Fisher 가 개발한 분산분석 ( ANalysis Of Variance) 을 이용하게 된다
# f값 = 그룹 간 분산(Between Variance) / 그룹 내 분산(Within Variance)
# 분자 부분의 분산을 비교 대상인 분모 부분의 분산과 비교하여 비율로써 나타낸 값.
# 독립변수는 범주형, 종속변수는 연속형

# 서로 독립인 세 집단의 평균 차이 검정 - 일원 분산 분석(one-way anova)
# 실습) 세 가지 교육방법을 적용하여 1 개월 동안 교육받은 교육생 80 명을 대상으로 실기시험을 실시. three_sample.csv
# 귀무 : 교육방법에 따른 시험점수에 차이가 없다. 
# 대립 : 교육방법에 따른 시험점수에 차이가 있다.
import urllib.request
import numpy as np
import pandas as pd 
from scipy import stats
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/three_sample.csv"
data = pd.read_csv(urllib.request.urlopen(url), delimiter=',', na_values=' ')
data = data.dropna()
print(data.head(3),data.shape)          # (80, 4)

#plt.boxplot(data.score)
#plt.hist(data.score)
#plt.show()

data = data.query('score <= 100')
print(data.shape)

#plt.hist(data.score)
#plt.show()

# 분산분석의 전제조건 : 3가지를 충족할 때 의미있다. 
# 독립성 : 각 집단은 서로 독립이어야 한다. (상관관계로 확인)
# 정규성 : 각 집단은 정규분포를 따라야 한다.  shapiro, stats.ks_2samp(롤모고로프 - 스미르노프)
# 불편성(등분산성) : 각 집단은 서로 분산이 일정해야 한다. 

print(data['method'].unique())  # [1 3 2]
result = data[['method','score']]
m1 = result[result['method']== 1]
m2 = result[result['method']== 2]
m3 = result[result['method']== 3]
print(m1[:3])
print(m2[:3])
print(m3[:3])
score1 = m1['score']
score2 = m2['score']
score3 = m3['score']
print(np.mean(score1),np.mean(score2),np.mean(score3))      # 67.38 68.35 68.87

print(' 정규성 검정 : 만족하면 anova, 만족하지 않으면 kruskal-wallis test')
print(stats.shapiro(score1).pvalue)      # 0.174 > 0.05이므로 정규성 만족
print(stats.shapiro(score2).pvalue)     # 0.331 > 0.05이므로 정규성 만족
print(stats.shapiro(score3).pvalue)     # 0.115 > 0.05이므로 정규성 만족
print(stats.ks_2samp(score1, score2).pvalue)     # 0.30
print(stats.ks_2samp(score1, score3).pvalue)     # 0.71
print(stats.ks_2samp(score2, score3).pvalue)    # 0.77

print(' 등분산성 검정 : 만족하면 anova, 만족하지 않으면 welch-anova')
print(stats.levene(score1, score2,score3).pvalue)       # 모수 검정     0.113 > 0.5 이므로 등분산성 만족
print(stats.bartlett(score1, score2,score3).pvalue)    # 비모수 검정   0.15
# 참고  : 등분산성을 만족하지 않은 경우 대처 방안
# 데이터를 normalization(정규화)으로 처리, standardzation(표준화)로 처리, transformation 경우에 따라 자연 log를 붙임

# 교차표 : 교육방법별 건수
ctab1 = pd.crosstab(index=data['method'], columns='count')
ctab1.index = ['방법1', '방법3', '방법2']
print(ctab1)

# 교차표 : 교육방법별 만족여부 건수
ctab2 = pd.crosstab(data.method, data.survey)
ctab2.columns=['만족', '불만족']
print(ctab2)

# anova_lm은 f통계량을 위해 회귀분석 결과를 사용
import statsmodels.api as sm
reg = ols('score ~ method', data).fit()     # r패턴 모방
# reg = ols("data['score'] ~ data['method']", data = data).fit()
table = sm.stats.anova_lm(reg, typ=1)
print(table)    # 분산 분석표 출력 
# 해석 : p-value 0.72 > 0.05 이므로 귀무가설 기각 실패. 교육방법에 따른 시험점수에 차이가 없다.

print()
# 사후 분석(post hoc) : anova 검증 결과 유의하다는 결론을 얻었을 때, 구체적으로 어떤 수준에서 평균 차이가 나는지를 검증하는 방법
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tkResult = pairwise_tukeyhsd(endog=data.score, groups=data.method)
print(tkResult)

tkResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()
 












