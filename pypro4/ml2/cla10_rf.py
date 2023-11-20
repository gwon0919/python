# RandomForestClassifier : DecisionTree 여러 개를 합쳐서 앙상블 모델로 운영 - bagging 알고리즘
# DecisionTree 결과값을 Voting을 통해 얻음. Boosting에 비해 성능은 떨어지나 과적합 처리가 효과적

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd 
from nltk.chunk.util import accuracy

# titanic data으로 연습
df = pd.read_csv("../testdata/titanic_data.csv")
print(df.head(2), df.shape)  # (891, 12)
print(df.isnull().any())

df = df.dropna(subset=['Pclass', 'Age', 'Sex'])
df_x = df[['Pclass', 'Age', 'Sex']]
print(df_x.head(2), df_x.shape)  # (714, 12)

df_y = df['Survived']
print(df_y.head(2))

print()
print(df['Sex'][:2])    # male : 1, female : 0  dummy 변수화
from sklearn.preprocessing import LabelEncoder # Categorical 데이터를 Numerical 로 변환(사전순)
df_x.loc[:,'Sex'] = LabelEncoder().fit_transform(df_x['Sex'])
# df_x['Sex'] = df_x['Sex'].apply(lambda x:1 if x == 'male' else 0)
print(df_x['Sex'][:2])
pd.set_option('display.max.columns', 500)
print(df_x.head(2))

# train / test split
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.2, random_state=12)

# model
model = RandomForestClassifier(criterion='entropy', n_estimators=100)  # 불순물 판단기준 - entropy
model.fit(train_x, train_y)

pred = model.predict(test_x)
print('예측값 : ', pred[:5])
print('실제값 : ', test_y[:5].ravel())

print('acc : ', sum(test_y == pred) / len(test_y))
from sklearn.metrics import accuracy_score
print('acc : ', accuracy_score(test_y, pred))

# 교차검증 ( KFold)
from sklearn.model_selection import cross_val_score
cross_vali = cross_val_score(model, df_x, df_y, cv=5)
import numpy as np
print('교차 검증 5회 실시한 정확도 평균 : ', np.round(np.mean(cross_vali), 3))
# Bagging(과적합 추정 모델을 결합해 이 과적합 효과를 줄임) - 임의화 의사결정 트리 앙상블 모델 : 예) RandomClassifier...
# 임의화(randomization)란 확률적 매커니즘을 통하여 실험개체를 비교하는 두 그룹,
# 즉 처리(treatement)되는 그룹과 대조(control)되는 그룹에 배치되도록 하는 것을 의미한다. 임의화 샘플링(복원 추출)

# 중요 변수(feature) 확인
print('특성(변수, feature) 중요도 : ', model.feature_importances_)
import matplotlib.pyplot as plt

# feature 중요도 시각화
def plot_feature_importance_func(model):
    n_features = df_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel('importance')
    plt.ylabel('feature name')
    plt.show()
    
plot_feature_importance_func(model)

























