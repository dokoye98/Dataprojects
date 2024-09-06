import pandas  as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection._split import train_test_split
from sklearn.tree import DecisionTreeClassifier
import sklearn.tree as tr

from sklearn.metrics import accuracy_score


excelfile = "diabetes.csv"
headers = ["Pregnacy","Glucose","Blood-Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function",
           "Age","Outcome"]

df = pd.read_csv(excelfile,names=headers)

#print(df.corr(method="pearson"))#are independent variables related -1 - 1

#df.plot.scatter(x= "Age", y= "BMI")
#df.plot.scatter(x="Outcome", y="Glucose")
#sns.pairplot(df,hue="Glucose")
#plt.show()

#print(df.Outcome.value_counts())
#print(df.describe())#only min value that should be zero is outcome and pregnancy

df_copy = df.copy(deep=True)

df_copy[["Glucose","Blood-Pressure", "Skin Thickness", "Insulin", "BMI",]] = df_copy[["Glucose","Blood-Pressure", "Skin Thickness", "Insulin", "BMI",]].replace(0,np.nan)

#print(df_copy.iloc[:,0].head())
#print(df_copy["Glucose"].describe())
#print(df_copy["Glucose"].isnull().sum())
df_copy["Glucose"].fillna(df_copy["Glucose"].mean(), inplace=True)
#print(df_copy["Glucose"].isnull().sum())
#print(df_copy["Skin Thickness"].describe())
df_copy["Blood-Pressure"].fillna(df_copy["Blood-Pressure"].mean(), inplace=True)
df_copy["Skin Thickness"].fillna(df_copy["Skin Thickness"].median(), inplace=True)#value for median and mean are so close
df_copy["Insulin"].fillna(df_copy["Insulin"].mean(), inplace=True)
df_copy["BMI"].fillna(df_copy["BMI"].mean(), inplace=True)
#print(df_copy.isnull().sum())

df_copy.boxplot(column=["BMI"])
#plt.show()

y = df_copy["Outcome"]
#print(sklearn.__version__)
#print(y.head())
ss = StandardScaler()

PRIMA = pd.DataFrame(ss.fit_transform( df_copy.drop(["Outcome"],axis=1),),columns=["Pregnacy","Glucose","Blood-Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function",
           "Age"])
#print(PRIMA)
#print(len(PRIMA.iloc[:,0])*0.75)
test = train_test_split

xtrain, xtest,ytrain,ytest = test(PRIMA,y,test_size=0.3,random_state = 42, stratify = y)

Dt = DecisionTreeClassifier(criterion= "entropy",random_state= 42)
Dt.fit(xtrain, ytrain)
pred = Dt.predict(xtest)

tr.plot_tree(Dt)
header1 = ["Pregnacy","Glucose","Blood-Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function",
           "Age"]



