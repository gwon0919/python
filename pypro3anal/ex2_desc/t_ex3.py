# 서로 대응인 두 집단의 평균 차이 검정 (paired samples t test)
# 처리 이전과 처리 이후를 각각의 모집단으로 판단하여 동일한 관찰 대상으로부터 처리 이전과 처리 이후를 1 1 로 대응시킨 두 집단으로 부터
# 의 표본을 대응표본 (paired sample) 이라고 한다
# 대응인 두 집단의 평균 비교는 동일한 관찰 대상으로부터 처리 이전의 관찰과 이후의 관찰을 비교하여 영향을 미친 정도를 밝히는데 주로 사용
# 하고 있다 집단 간 비교가 아니므로 등분산 검정을 할 필요가 없다
# 예) 6개월 기간 동안 초코파이를 먹기 전후의 몸무게가 같은가? 

from scipy import stats
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# 실습3) 복부 수술 전 9 명의 몸무게와 복부 수술 후 몸무게 변화

# 귀무 : 복부 수술 전 9명의 몸무게와 복부 수술 후 몸무게 변화에 차이가 없다.
# 대립 : 복부 수술 전 9명의 몸무게와 복부 수술 후 몸무게 변화에 차이가 있다.

baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

print(np.mean(baseline))
print(np.mean(follow_up))

plt.bar(np.arange(2), [np.mean(baseline),np.mean(follow_up)])
#plt.show()

pair_sample = stats.ttest_rel(baseline, follow_up)
print('t-value : %.5f, p-value : %.5f'%pair_sample) 
# 판정 : p-value : 0.00633 < 0.05 이므로 귀무 가설 기각. 몸무게 변화에 차이가 있다.

print('-------------2-----------------')
# [two-sample t 검정 : 문제2]  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.

# 귀무 : 남자와 여자는 혈관 내의 콜레스테롤 양에 차이가 없다.
# 대립 : 남자와 여자는 혈관 내의 콜레스테롤 양에 차이가 있다.

남자 = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
여자 = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]

np.random.seed(0)  # 난수 발생 시드 설정 (원래 실행 결과와 동일한 결과를 얻기 위해)
msample = np.random.choice(남자, 15, replace=False)
wsample = np.random.choice(여자, 15, replace=False)
print(msample)
print(wsample)

pair_sample2 = stats.ttest_ind(msample, wsample)
print('t-value : %.5f, p-value : %.5f'%pair_sample2)
# 판정 : p-value : 0.88 > 0.05 귀무 채택

print('-------------3--------------')
# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.

# 귀무 : 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하지 않는다.
# 대립 : 총무부, 영업부 직원의 연봉의 평균에 차이가 존재한다.

import MySQLdb
import pickle

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select buser_name, jikwon_pay from jikwon inner join buser on buser_no = buser_num
    """
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns=['buser_name', 'jikwon_pay'])
    #print(df)

    cdata = df[df['buser_name'] == '총무부']['jikwon_pay']
    ydata = df[df['buser_name'] == '영업부']['jikwon_pay']
    
    print(stats.shapiro(cdata).pvalue)      # 0.026 < 0.05이므로 정규성 불만족
    print(stats.shapiro(ydata).pvalue)      # 0.025 < 0.05이므로 정규성 불만족
    
    pair_sample3 = stats.mannwhitneyu(cdata,ydata)
    # pair_sample3 = stats.ttest_ind(cdata, ydata)
    print('t-value : %.5f, p-value : %.5f'%pair_sample3)
    # 판정 : p-value : 0.47 > 0.05 이므로 귀무 채택. 연봉의 평균에 차이가 존재하지 않는다.
  
except Exception as e:
    print('처리 오류 :', e)

finally:
    cursor.close()
    conn.close()
  
print('------------------4--------------------')
# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?  

# 귀무 : 학급의 학업능력이 변화하지 않았다.
# 대립 : 학급의 학업능력이 변화했다.

midtest = [ 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
finaltest = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]
  
print(np.mean(midtest), np.mean(finaltest))     # 74.17 / 81.67

pair_sample4 = stats.ttest_ind(midtest, finaltest)
print('t-value : %.5f, p-value : %.5f'%pair_sample4) 
# 판정: p-value : 0.18 > 0.05 이므로 귀무 채택. 학급의 학업능력이 하지 않았다.  
  
  
  
  
  

  
  
  
  
