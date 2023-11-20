
# [Randomforest 문제1] 
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)

# dataset은 winequality-red.csv 
import pandas as pd 
import numpy as np


data=pd.read_csv("../testdata/wine.csv")
# Input variables (based on physicochemical tests):
'''
 1 - fixed acidity
 2 - volatile acidity 
 3 - citric acid
 4 - residual sugar
 5 - chlorides
 6 - free sulfur dioxide
 7 - total sulfur dioxide
 8 - density
 9 - pH
 10 - sulphates
 11 - alcohol
 Output variable (based on sensory data):
 12 - quality (score between 0 and 10)
 '''
print(data.head(2))
