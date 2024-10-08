# -*- coding: utf-8 -*-
"""IRIS Flower Classification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EvK5G3oF_ncW-M7arV6Y1Es1k7HudYdy
"""

# Commented out IPython magic to ensure Python compatibility.
#import all the essential libraries for project
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# %matplotlib inline

# load the data from the CSV file
columns = ['sepal length','sepal width','petal length','petal width','Class_labels']
df = pd.read_csv('IRIS.csv',names = columns)
df.head(150)

df.describe()

# Visualize the whole dataset
sns.pairplot(df,hue='Class_labels')

# separate the features and target
data = df.values
X = data[:,0:4]
Y = data[:,4]

# split the data to train and test data
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2)
print(X_train)

# support vector machine Algorithm
from sklearn.svm import SVC
model_svc = SVC()
model_svc.fit(X_train,Y_train)

# calculate the accuracy
predcition1 = model_svc.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,predcition1)*100)
for i in range(len(predcition1)):
  print(Y_test[i],predcition1[i])

# Logistic Regression
from sklearn.linear_model import LogisticRegression
model_LR = LogisticRegression()
model_LR.fit(X_train,Y_train)

# calculate the accuracy
prediction2 = model_LR.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,prediction2)*100)
for i in range(len(predcition1)):
  print(Y_test[i],predcition1[i])

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
model_DT = DecisionTreeClassifier()
model_DT.fit(X_train,Y_train)

# Accuracy Score
prediction3 = model_svc.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,prediction2)*100)
for i in range(len(prediction2)):
  print(Y_test[i],prediction2)

# A detailed classification report
from sklearn.metrics import classification_report
print(classification_report(Y_test,predcition1))

# prediction of the species from input vector
X_new = np.array([[3,2,1,0.2],[4.9,2.2,3.8,1.1],[5.3,2.5,4.6,1.9]])
prediction = model_svc.predict(X_new)
print("Prediction Of Species:{}".format(prediction))