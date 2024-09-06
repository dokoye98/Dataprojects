from flask import Flask,request,render_template
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

excelfile = "diabetes.csv"
headers = ["Pregnacy","Glucose","Blood-Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function",
           "Age","Outcome"]

df = pd.read_csv(excelfile,names=headers)

#print(df["Age"].value_counts())
X = df.copy()
X = X.drop(columns="Outcome", axis=1)
Y = df["Outcome"]
#print(Y.value_counts())

scaler = StandardScaler()
scaler.fit(X)
standerdised = scaler.transform(X)
#print(standerdised)
X = standerdised
xtrain,xtest,ytrain,ytest = train_test_split(X,Y, test_size=0.2,stratify=Y, random_state=2)
#print(xtrain.shape, xtest.shape)
classifier = svm.SVC(kernel="linear")
classifier.fit(xtrain,ytrain)
XtrAccur = classifier.predict(xtrain)
trainaccuracy = accuracy_score(XtrAccur,ytrain)
#print(trainaccuracy)

XtestAccur = classifier.predict(xtest)
testaccuracy = accuracy_score(XtestAccur,ytest)
#print(testaccuracy)
input_data = (3,171,72,33,135,33.3,0.199,24,0,95,85,25,36,37.4,0.247,24,8,155,62,26,495,34,0.543,46,1,89,76,34,37,31.2,0.192,23)
#print(np.random.randint(1,700))
inputarr = np.asarray(input_data)
reshapedinput = inputarr.reshape(4,8)
stand = scaler.transform(reshapedinput)
#print(reshapedinput[:,0])
#print(stand)
predict = classifier.predict(stand)
diabetic = 0
nondiabetic = 0
for x in range(len(predict)):
    if predict[x] == 0:
        nondiabetic +=1
        
    else:
        diabetic +=1

print(diabetic , nondiabetic)



    
    
    
