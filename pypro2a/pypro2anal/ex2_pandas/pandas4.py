# pandas로 파일 읽기
import pandas as pd

df = pd.read_csv('../testdata/ex1.csv')
print(df, type(df))
print(df.info())
print()
df = pd.read_table('../testdata/ex1.csv', sep=',')
print(df.info())
print()
df = pd.read_table('../testdata/ex2.csv', header=None)
print(df)
df = pd.read_table('../testdata/ex2.csv', header=None, names=['col1','col2'])
print(df)
print()
df = pd.read_table('../testdata/ex2.csv', header=None, names=['a','b','c','d','msg'], index_col='msg')
print(df)
print()
# df = pd.read_csv('../testdata/ex3.txt')
df = pd.read_table('../testdata/ex3.txt', sep=' \s') # sep= ' ' sep='정규표현식
# \s : space를 표현라며 공백 문자를 의미한다.
# \S: non space를 표현하며 공백 문자가 아닌 것을 의미한다.
print(df)
print(df.info())
print(df.describe())
print()
df = pd.read_table('../testdata/ex3.txt', sep=' \s+', skiprows=(1,3))
print(df)

print()
df = pd.read_fwf('../testdata/data_fwt.txt', widths=(10,3,5), header=None, names=('date','name','price'))
print(df)

print()
# 대용량의 자료를 chuck(묶음) 단위로 할당해서 처리 가능
test = pd.read_csv('../testdata/data_csv2.csv', header=None, chunksize=3)
print(test)         # TextFileReader object (텍스트 파서 객체)

for p in test:
    #print(p)
    print(p.sort_values(by=2, ascending=True))

print('\n\nDataFrame 저장')
items = {'apple':{'count1':10, 'price': 1500}, 'orange':{'count1':5, 'price': 1000}}
df = pd.DataFrame(items)
print(df)
#print(df.to_html())
#print(df.to_json())
#print(df.to_clipboard())
#print((df.to_csv()))
df.to_csv('test1.csv', sep=',')
df.to_csv('test2.csv', sep=',', index=False)
df.to_csv('test3.csv', sep=',', index=False,header=False)

print()
# 문제 3
print('문제 3-(1)')
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]

# 'Age' 열을 기준으로 나이대를 나누고 'AgeGroup' 열을 생성
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 각 나이대별 생존자 수 계산
age_group_survival = df.groupby('AgeGroup')['Survived'].sum()

print(age_group_survival)
print()
print('문제 3-(2)')
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')

pivot_table = df.pivot_table(values='Survived', index=['Sex', 'Age'], columns='Pclass', aggfunc='mean')

# 생존율을 백분율로 변환 (소수 둘째 자리까지)
pivot_table = pivot_table.apply(lambda x: x * 100).round(2)

print(pivot_table)
print()


print('문제4-(1)')
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/human.csv')
print(df)

print('strip() 함수를 사용하여 공백 제거')
df.columns = df.columns.str.strip()
print(df)
print()

print('Group인 NA인 행 삭제')
df = df[df['Group'].str.strip() != 'NA']
print(df)
print()

print('Career, Score 칼럼을 추출하여 DataFrame 을 작성')
df = df[['Career', 'Score']]
print(df)
print()

print('Career, Score 칼럼의 평균 계산')
avg_career = df['Career'].mean()
avg_score = df['Score'].mean()
print()

# 결과 출력
print(df)
print(f'평균 Career: {avg_career}')
print(f'평균 Score: {avg_score}')



# tips.csv 파일 읽기
tips = pd.read_csv('../testdata/tips.csv')

print(tips.info())
print(tips.head(3))
print(tips.columns)
print(tips.describe())
print()

# 흡연자, 비흡연자 수 계산
smoke_counts = tips['smoker'].value_counts()
print("\n흡연자, 비흡연자 수:")
print(smoke_counts)
print()

# 요일 칼럼의 유일한 값 출력
uni_days = tips['day'].unique()  # pd.unique(tips['day'])
print("\n요일 칼럼의 유일한 값:")
print(uni_days)

















