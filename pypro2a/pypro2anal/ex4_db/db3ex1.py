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

# 문제 5

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no,jikwon_name,buser_name,jikwon_pay,jikwon_jik
        from jikwon j join 
        buser b on b.buser_no=j.buser_num
    """
    cursor.execute(sql)
    #     - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
    df = pd.DataFrame(cursor.fetchall(),
    columns=['jikwon_no', 'jikwon_name', 'buser_name', 'jikwon_pay', 'jikwon_jik'])
    print(df)
    print()
#     - DataFrame의 자료를 파일로 저장
    with open('jData.csv', mode='w', encoding='utf-8') as jobj:
        writer = csv.writer(jobj)
        for r in cursor:
            writer.writerow(r)

    print()
#     - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    print('부서명 별 연봉의 합과 최대/최소값')
    hap = df.groupby('buser_name')['jikwon_pay'].sum()
    result = df.groupby('buser_name')['jikwon_pay'].agg(['max', 'min'])
    print(hap, result)
    
    print()
    #     - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
    ctab = pd.crosstab(df['buser_name'], df['jikwon_jik'])
    print(ctab)
    
    print()
#     - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    jAvg = df.groupby('buser_name')['jikwon_pay'].mean()
    print(jAvg)

    jAvg.plot(kind='barh', figsize=(10, 6), color='pink')
    plt.xlabel('평균 연봉')
    plt.ylabel('부서명')
    plt.title('부서명 별 평균 연봉')
    plt.show()
    
#     - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    sql2 = """
        SELECT j.jikwon_name, IFNULL(g.gogek_no, '담당 고객 X') AS gogek_no, IFNULL(g.gogek_name, '담당 고객 X') AS gogek_name, IFNULL(g.gogek_tel, '담당 고객 X') AS gogek_tel
        FROM jikwon j
        LEFT JOIN gogek g ON j.jikwon_no = g.gogek_damsano
    """
    
    cursor.execute(sql2)
    
    columns = ['직원명', '고객번호', '고객명', '고객전화']
    data2 = cursor.fetchall()
    df2 = pd.DataFrame(data2, columns=columns)
    
    print(df2)

    print()
    # - pivot_table을 사용하여 성별 연봉의 평균을 출력
    sql3 = """
        SELECT jikwon_name, jikwon_gen, jikwon_pay,jikwon_jik
        FROM jikwon 
    """
    cursor.execute(sql3)
    columns = ['직원명', '성별', '연봉','직급']
    data3 = cursor.fetchall()
    df = pd.DataFrame(data3, columns=columns)
    
    gAvg = df.pivot_table(index='성별', values='연봉', aggfunc='mean')
    print(gAvg)
    
    # - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
    gAvg.plot(kind='bar', figsize=(6, 6), color='skyblue')
    plt.xlabel('성별')
    plt.ylabel('평균 연봉')
    plt.title('성별 별 평균 연봉')
    plt.xticks(rotation=0)  # x축 레이블을 0도 회전
    plt.show()
    print()
    # - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))
    btab = pd.crosstab(df['성별'], df['직급'], margins=True)
    print(btab)

except Exception as e:
    print('처리 오류 :', e)

finally:
    cursor.close()
    conn.close()











