# -*- coding: utf-8 -*-
"""Ayman jamal attili.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ey8mBBc78_VcOA-mq1uDRiBmIOQZ-gqv
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv( "https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv")

data.head()

data.describe()

data.info()

data.isnull().sum()

plt.bar(x=data['Hours'] , height=data['Scores'] )
plt.title('Hours vs Percentage')  
plt.xlabel('Studying Hours')  
plt.ylabel('Score Percentage out of 100% ') 
plt.show()

plt.scatter( data['Hours'],data['Scores'])
plt.title('Hours vs Percentage')  
plt.xlabel('Studying Hours')  
plt.ylabel('Score Percentage out of 100% ') 
plt.show()

sns.boxplot(data['Hours'])
plt.title('check outliers of Hours')

sns.boxplot(data['Scores'])
plt.title('check outliers of scores')

x = data.drop('Scores',axis=1)
y = data['Scores']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

lin = LinearRegression( )
lin.fit(x_train,y_train)
pred = lin.predict(x_test) 
print(mean_absolute_error( y_test, pred))

from sklearn.model_selection import cross_val_score
scores1=cross_val_score(lin, x, y,scoring='neg_mean_absolute_error' ,cv=10 )
scores1.mean()

print(f"The predicted score when the student studying 9.25 hour/day is : {lin.predict([[9.25]])}")