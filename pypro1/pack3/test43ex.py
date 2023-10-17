# jikwon 테이블을 대상으로 사번과 이름을 입력(로그인)해 해당 자료가 있다면 
# 해당 직원이 근무하는 부서직원을 직급별 오름차순으로 모두 출력. 직급이 같으면 이름별 오름차순출력.
# 출력 형태 : 사번, 이름, 부서명, 직급, 성별
#           5   홍길동 총무부  대리  남
#          인원수 : * 명
# 다음으로 해당직원이 관리하는 고객자료 출력
# 출력 형태 : 고객번호 고객명  고객전화     나이
#            3    신기해 111-1111   23
#          관리고객수 : * 명

import MySQLdb

# 데이터베이스 연결 설정(config) 로딩
import pickle

with open('mydb.dat', 'rb') as config_file:
    config = pickle.load(config_file)

def login():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        # 사용자로부터 사번과 이름 입력 받기
        jikwon_no = input('사번 입력: ')
        jikwon_name = input('이름 입력: ')

        # 입력된 사번과 이름을 이용하여 직원 정보 조회
        sql = """
            SELECT jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_gen
            FROM jikwon 
            WHERE jikwon_no = '{0}' AND jikwon_name = '{1}'
        """.format(jikwon_no,jikwon_name)
        cursor.execute(sql)
        employee = cursor.fetchall()

        if len(employee) ==0:
            print('해당 직원 정보가 없습니다.')
            return

        #print(f'사번: {employee[0]}, 이름: {employee[1]}')

        # 직원의 부서 및 직급 정보 가져오기
        buser_num = employee[2]
        jikwon_jik = employee[3]

        # 부서 직원을 직급 및 이름을 기준으로 정렬하여 가져오기
        sql = """
            SELECT jikwon_no, jikwon_name, buser_name, jikwon_jik,jikwon_gen
            FROM jikwon inner join buser on buser_num = buser_no
            WHERE buser_num = {0}
            ORDER BY jikwon_jik ASC, jikwon_name ASC
        """.format(buser_num)
        
        
        cursor.execute(sql)
        department_employees = cursor.fetchall()

        print('\n부서 직원 목록:')
        for jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen  in department_employees:
            print(jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen)
        print('인원수 : ' + str(len(department_employees)))
        
        # 해당 직원이 관리하는 고객 정보 가져오기
        sql_gogek = """
        SELECT gogek_no, gogek_name, gogek_tel, TIMESTAMPDIFF(YEAR, SUBSTR(gogek_jumin, 1, 6), CURDATE()) AS gogek_age
        FROM gogek
        INNER JOIN jikwon ON jikwon_no = gogek_damsano
        WHERE gogek_damsano = {0}
        """.format(jikwon_no)
        
        
        # print("Debug: SQL Query for Customers:", sql_gogek)  # 디버깅용 출력문 추가
        
        cursor.execute(sql_gogek)
        managed_customers = cursor.fetchall()

        print('\n고객 목록:')
        for gogek_no, gogek_name, gogek_tel, gogek_age in managed_customers:
            print(gogek_no, gogek_name, gogek_tel, gogek_age)
    
        print('인원수 : ' + str(len(managed_customers)))
        
    except Exception as e:
        print('에러 발생:', e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    login()
