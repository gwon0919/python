# 파일 입출력
import os 
print(os.getcwd())      # 현재 모듈의 경로명 반환

try:
    print('파일 읽기')
    # mode ='r','w','a'/ read write append binary text
    #f1 = open(r'C:\Users\acorn\git\python\pypro1\pack3\test37.txt', mode ='r', encoding='utf-8')
    #f1 = open(os.getcwd()+ r'\test37.txt', mode = 'r', encoding='utf-8')
    f1 = open(r'test37.txt',mode ='r', encoding='utf-8')
    print(f1)   # 파일 객체 확인
    print(f1.read())
    f1.close()
    
    print('파일 저장--')
    f2 = open(r'test37w.txt', mode='w', encoding='utf-8')
    f2.write('나의 친구들\n')
    f2.write('홍길동,한국인')
    f2.close()
    print('저장 성공')
    
    print('파일 추가--')
    f2 = open(r'test37w.txt', mode='a', encoding='utf-8')
    f2.write('\n손오공')
    f2.write('\n사오정')
    f2.write('\n저팔계')
    f2.close()
    print('저장 성공')
    
    print('저장된 파일 읽기')
    f3 = open(r'test37w.txt', mode='r', encoding='utf-8')
    print(f3.readline())
    print(f3.readline(1),f3.readline(2)) # 한 행의 부분 문자 읽기
    lines=f3.readlines()                 # 모든 행을 읽어 list 타입으로 저장
    print(lines)    
    f3.close()
    
except Exception as e:
    print('파일 처리 에러: ', e)

