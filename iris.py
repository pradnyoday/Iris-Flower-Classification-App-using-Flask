# -*- coding: utf-8 -*-
"""iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1phivvUgRxDv8YoRu-amzKahsQzOCpoMS
"""

from sklearn import datasets
iris = datasets.load_iris()

"""Now assign the data and target"""

x = iris.data
y = iris.target

print(iris.feature_names)

"""Split the data into training and testing data"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)

"""Now its time to Build Model"""

from sklearn import tree
classifier=tree.DecisionTreeClassifier()

"""Train the model"""

build = classifier.fit(x_train,y_train)

"""Predictions"""

preds = classifier.predict(x_test)
print(preds)

"""Calculate Accuracy"""

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,preds)*100,"%")

p = classifier.predict([[5.9,3. , 5.1, 1.8]])
print(p)