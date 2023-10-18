import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
def jik():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        jikwon_jik = input("직급을 입력하세요: ")

        sql = """
            SELECT jikwon_no, jikwon_name, jikwon_jik, buser_num
            FROM jikwon
            WHERE jikwon_jik = %s
        """

        cursor.execute(sql, (jikwon_jik,))
        datas = cursor.fetchall()

        if not datas:
            print(jikwon_jik + '직급은 없어요')
            return  
        
        print("직원 목록:")
        for jikwon_no, jikwon_name, jikwon_jik, buser_num in datas:
            print(jikwon_no, jikwon_name, jikwon_jik, buser_num)
    
    except Exception as e:
        print('에러 발생:', e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    jik()
