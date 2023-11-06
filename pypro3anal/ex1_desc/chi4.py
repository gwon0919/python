# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오 
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
import pandas as pd 
import scipy.stats as stats 

data = pd.read_csv("../testdata/cleanDescriptive.csv")  # 표본 자료
print(data.head(10))
#print(data1.columns)
data1 = data.dropna()
#print(data1.info())
ctab = pd.crosstab(index=data1['level'], columns=data1['pass'])
print(ctab)
chi2, p, df, _ = stats.chi2_contingency(ctab)
print('chi2:{}, p:{}, df:{} '.format(chi2, p, df))
# 판정 : p:0.02029 < 0.05 이기 때문에 유의한 수준(α=0.05)에서 귀무가설을 기각한다. 




print('----------------')
# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
# 그렇다면 jikwon_jik과 jikwon_pay 간의 관련성 여부를 통계적으로 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.

# 귀무 :
# 대립 : 

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
        select jikwon_pay,jikwon_jik from jikwon 
    """
    cursor.execute(sql)
    #     - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
    df = pd.DataFrame(cursor.fetchall(),
    columns=['jikwon_pay', 'jikwon_jik'])
    #print(df)
    jik_mapping = {
        '이사' : 1,
        '부장' : 2,
        '과장' : 3,
        '대리' : 4,
        '사원' : 5
        }
    
    
except Exception as e:
    print('처리 오류 :', e)

finally:
    cursor.close()
    conn.close()
















