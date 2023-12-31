# -*- coding: utf-8 -*-
"""Heart Disease.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GVTkgaYW1po8KSujY1biVZvawEIrKq3A
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

heart_data=pd.read_csv('/content/heart0.0.csv')

x = heart_data.drop(columns='target', axis=1)
y = heart_data['target']

sns.heatmap(heart_data,annot=True)

sns.pairplot(heart_data)

sns.countplot(x='target',data=heart_data)
plt.xticks([0,1],['Diseased','Healthy'])
plt.title("Result distribution of patients")
plt.show()

sns.displot(x='Age',kde=True,data=heart_data)
plt.title("Age distribution of patients")
plt.grid(True)
plt.show()

sns.countplot(x='gender',data=heart_data)
plt.xticks([0,1],['Female','Male'])
plt.title("Gender distribution of patients")
plt.show()

sns.countplot(x='cp',data=heart_data)
plt.xticks([0,1,2,3],['TA','ATA','NAP','ASY'])
plt.title("Chest Pain distribution of patients")
plt.show()

sns.displot(x='trestbps',data=heart_data,kde=True)
plt.title("Blood Pressure distribution of patients")
plt.grid(True)
plt.show()

sns.displot(x='chol',data=heart_data,kde=True)
plt.title("Cholesterol distribution of patients")
plt.grid(True)
plt.show()

sns.countplot(x='restecg',data=heart_data)
plt.xticks([0,1,2],['Normal','ST','LVH'])
plt.title("Electrocardiographic distribution of patients")
plt.show()

sns.displot(x='oldpeak',data=heart_data,kde=True)
plt.title("ST depression distribution of patients")
plt.grid(True)
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=None)

model1 = LogisticRegression(solver='lbfgs', max_iter=10000)
model1.fit(x_train, y_train)
x_train_prediction1 = model1.predict(x_train)
x_test_prediction1 = model1.predict(x_test)
training_data_accuracy1 = accuracy_score(x_train_prediction1, y_train)
testing_data_accuracy1 = accuracy_score(x_test_prediction1, y_test)
print('accuracy on training data: ', training_data_accuracy1)
print('accuracy on testing data: ', testing_data_accuracy1)

model2 = KNeighborsClassifier()
model2.fit(x_train, y_train)
x_train_prediction2 = model2.predict(x_train)
x_test_prediction2 = model2.predict(x_test)
training_data_accuracy2 = accuracy_score(x_train_prediction2, y_train)
testing_data_accuracy2 = accuracy_score(x_test_prediction2, y_test)
print('accuracy on training data: ', training_data_accuracy2)
print('accuracy on testing data: ', testing_data_accuracy2)

model3 = SVC(random_state=None)
model3.fit(x_train, y_train)
x_train_prediction3 = model3.predict(x_train)
x_test_prediction3 = model3.predict(x_test)
training_data_accuracy3 = accuracy_score(x_train_prediction3, y_train)
testing_data_accuracy3 = accuracy_score(x_test_prediction3, y_test)
print('accuracy on training data: ', training_data_accuracy3)
print('accuracy on testing data: ', testing_data_accuracy3)

model4 = GaussianNB()
model4.fit(x_train, y_train)
x_train_prediction4 = model4.predict(x_train)
x_test_prediction4 = model4.predict(x_test)
training_data_accuracy4 = accuracy_score(x_train_prediction4, y_train)
testing_data_accuracy4 = accuracy_score(x_test_prediction4, y_test)
print('accuracy on training data: ', training_data_accuracy4)
print('accuracy on testing data: ', testing_data_accuracy4)

model5 = RandomForestClassifier(random_state=None)
model5.fit(x_train, y_train)
x_train_prediction5 = model5.predict(x_train)
x_test_prediction5 = model5.predict(x_test)
training_data_accuracy5 = accuracy_score(x_train_prediction5, y_train)
testing_data_accuracy5 = accuracy_score(x_test_prediction5, y_test)
print('accuracy on training data: ', training_data_accuracy5)
print('accuracy on testing data: ', testing_data_accuracy5)

model6 = XGBClassifier()
model6.fit(x_train, y_train)
x_train_prediction6 = model6.predict(x_train)
x_test_prediction6 = model6.predict(x_test)
training_data_accuracy6 = accuracy_score(x_train_prediction6, y_train)
testing_data_accuracy6 = accuracy_score(x_test_prediction6, y_test)
print('accuracy on training data: ', training_data_accuracy6)
print('accuracy on testing data: ', testing_data_accuracy6)

m=[training_data_accuracy1,training_data_accuracy2,training_data_accuracy3,training_data_accuracy4,training_data_accuracy5,training_data_accuracy6]
n=[testing_data_accuracy1,testing_data_accuracy2,testing_data_accuracy3,testing_data_accuracy4,testing_data_accuracy5,testing_data_accuracy6]
lebel=['LR','KNN','SVM','NBC','RF','XGB']
plt.plot(lebel,m,label='training')
plt.plot(lebel,n,label='testing')
plt.xlabel('Algorithm')
plt.ylabel('Accuracy Rate')
plt.title('Accuracy Rate of Different Algorithm')
plt.legend()
plt.grid(True)
plt.show()

#input_data = (40,1,2,140,289,0,0,172,0,0,1)
#input_data_as_numpy_array = np.asarray(input_data)
#input_data_reshape = input_data_as_numpy_array.reshape(1, -1)
input_data=[]
input_data.append(int(input("Age: ")))
input_data.append(int(input("Gender (Male=1, Female=0): ")))
input_data.append(int(input("ChestPain (typical angina=1; atypical angina=2; non-anginal pain=3; asymptomatic=4): ")))
input_data.append(int(input("Resting Blood Pressure: ")))
input_data.append(int(input("Cholesterol: ")))
input_data.append(int(input("Fasting Blood Pressure: ")))
input_data.append(int(input("Resting electrocardiographic results: ")))
input_data.append(int(input("Maximum heart rate achieved: ")))
input_data.append(int(input("Exercise induced angina: ")))
input_data.append(int(input("ST depression induced by exercise relative to rest: ")))
input_data.append(int(input("The slope of the peak exercise ST segment: ")))
input_data = np.array(input_data)
#print(input_data)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

print("Select Algorithm(LR=1,KNN=2,SVM=3,NBC=4,RF=5,XGB=6): ")
val=int(input())
if val == 1:
  prediction = model1.predict(input_data_reshape)
  print("Logistic Regression Algorithm")
  if prediction[0] == 0:
    print('Healthy')
  else:
    print('Heart deceased')
elif val == 2:
  prediction = model2.predict(input_data_reshape)
  print("K-Nearest Neighbours Algorithm")
  if prediction[0] == 0:
    print('Healthy')
  else:
    print('Heart deceased')
elif val == 3:
  prediction = model3.predict(input_data_reshape)
  print("Support Vector Machine Algorithm")
  if prediction[0] == 0:
    print('Healthy')
  else:
    print('Heart deceased')
elif val == 4:
  prediction = model4.predict(input_data_reshape)
  print("Naive Bayes Classifier Algorithm")
  if prediction[0] == 0:
    print('Healthy')
  else:
    print('Heart deceased')
elif val == 5:
  prediction = model5.predict(input_data_reshape)
  print("Random Forest Algorithm")
  if prediction[0] == 0:
    print('Healthy')
  else:
    print('Heart deceased')
elif val == 6:
  prediction = model6.predict(input_data_reshape)
  print("XGBoost Algorithm")
  if prediction[0] == 0:
    print('Healthy')
  else:
    print('Heart deceased')