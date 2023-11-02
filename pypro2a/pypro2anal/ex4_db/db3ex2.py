import MySQLdb
import pickle
import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False  # 한글 처리때 음수가 깨지는 것을 방지하기 위해 사용
import seaborn as sns
import sys

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

#  문제 6
# 1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오. (join)
#        : 부서번호, 직원명 순으로 오름 차순 정렬 
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no,jikwon_name,buser_name,jikwon_jik,jikwon_pay, 
        CAST(DATEDIFF(NOW(), jikwon_ibsail) / 365 AS SIGNED) AS jikwon_ibsa
        from jikwon j join 
        buser b on b.buser_no=j.buser_num
    """
    cursor.execute(sql)
   
    df = pd.DataFrame(cursor.fetchall(),
    columns=['jikwon_no', 'jikwon_name', 'buser_name', 'jikwon_jik', 'jikwon_pay','jikwon_ibsa'])
    print(df)
    print()
# 2) 부서명, 직급 자료를 이용하여  각각 연봉합, 연봉평균을 구하시오.
    hap = df.groupby('buser_name')['jikwon_pay'].sum()
    print(hap)
    print('연봉 평균 : ', df.loc[:, 'buser_name'].value_counts())
    
 # 3) 부서명별 연봉합, 평균을 이용하여 세로 막대 그래프 출력
    avg = df.groupby('buser_name')['jikwon_pay'].mean()
    hap.plot(kind='bar', figsize=(8, 6), color='skyblue', title='부서별 연봉 합')
    plt.xlabel('부서명')
    plt.ylabel('연봉 합')
    plt.xticks(rotation=45)
    plt.show()

    avg.plot(kind='bar', figsize=(8, 6), color='lightcoral', title='부서별 연봉 평균')
    plt.xlabel('부서명')
    plt.ylabel('연봉 평균')
    plt.xticks(rotation=45)
    plt.show()

    # 4) 성별, 직급별 빈도표 출력
    crosstab = pd.crosstab(df['buser_name'], df['jikwon_jik'], margins=True)
    print("성별, 직급별 빈도표:")
    print(crosstab)
    
except Exception as e:
    print('처리 오류 :', e)

finally:
    cursor.close()
    conn.close()

