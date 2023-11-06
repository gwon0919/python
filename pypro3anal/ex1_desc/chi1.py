# 교차분석(카이 제곱 분석, 카이스퀘어, x²) 가설검정
# 카이제곱 분포는 데이터의 분산이 쳐져있는 모습을 분포로 만든 것.
# 명목, 서열 척도와 같은 범주형 자료를 대상으로 교차빈도에 대한 기술통계량을 제공해 줌. 
# 교차 빈도에 대한 통계적 유의성을 검증해 주는 추론통계 분석 방법이다.
# chi² = (관측값 - 기대값) 제곱의 합 / 기대값
# 그룹이 한 개 : 일원 카이 제곱 검정 -> 적합도(선호도)를 검정 - 교차 분할표 사용x
# 그룹이 두 개 : 이원 카이 제곱 검정 -> 두 집단 간의 독립성(동질성) 검정 - 일반적으로 교차 분할표 사용

# 수식을 이용하는 방법과 함수를 사용하는 방법 두 가지 모두 실습
# 공부하는 안하는 집단, 합격 / 불합격
import pandas as pd 

data = pd.read_csv("../testdata/pass_cross.csv", encoding='euc-kr')
print(data.head(3))
print(len(data))
# 귀무가설 : 벼락치기 공부하는 것과 합격 여부는 관계가 없다. 
# 대립가설 : 벼락치기 공부하는 것과 합격 여부는 관계가 있다.
print(data[(data['공부함']==1) & (data['합격']==1)].shape[0])  # 18
print(data[(data['공부함']==1) & (data['불합격']==1)].shape[0]) # 7

# 수식을 이용하는 방법
print('빈도표 작성')
ctab = pd.crosstab(index=data['공부안함'], columns= data['불합격'], margins=True)
ctab.columns = ['합격', '불합격', '행합']
ctab.index=['공부함', '공부안함', '열합']
print(ctab)
print('기대값 작성')         # 기댓값은 확률변수에 대해 평균적으로 기대하는 값
# 기대돗수 = ( 각 행의 주변합) * (각 열의 주변합) / 총합 : 전체 표본 수

print(25 * 30 / 50)
chi2 = (18-15)** 2/15 + (7-10) **2 / 10 + (12-15 )**2 /15 + (13-10)**2 /10 
print('chi²', chi2) #  3.0
# 임계값? - 카이제곱표를 이용
# df(자유도) = N(사례수) - K(통계적 제한 조건 수) 
# df = (행의 갯수 - 1 ) * (열의 갯수 - 1)    (2-1)*(2-1)= 1
# 해석 : cv = 3.84, chi² = 3.0 이므로  귀무기각 취소 (귀무채택)
# 벼락치기 공부하는 것과 합격 여부는 관계가 없다. 라는 결론을 얻을 수 있다.
# 귀무가설이 통계적으로 유의하다. 검증에 사용된 데이터는 우연히 발생되었다. 

print('----------------')
# 함수(메소드)를 사용하는 방법
import scipy.stats as stats
ctab = pd.crosstab(index=data['공부안함'], columns= data['불합격'])
ctab.columns = ['합격', '불합격']
ctab.index=['공부함', '공부안함']
print(ctab)

print(stats.chi2_contingency(ctab))
chi2, p, df, expected = stats.chi2_contingency(ctab)
print('p-value : ', p)
# 해석 : p-value(0.148) > α(0.05)이므로 귀무가설 채택
















     

