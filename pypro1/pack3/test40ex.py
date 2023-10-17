# test40su.txt 파일을 한 행 씩 읽어 각 행의 숫자의 합을 출력하시오

try:
    with open(r'test40su.txt', mode='r') as obj1:
        line = obj1.readline()
        for line in obj1:
            # 각 행의 숫자들을 분할하고 합계 계산
            numbers = [float(x) for x in line.split()]
            total = sum(numbers)
            print('합계: ', total)
except Exception as e:
    print('파일 처리 오류 : ', e)