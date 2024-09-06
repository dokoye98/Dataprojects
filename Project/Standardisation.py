from sklearn.preprocessing import StandardScaler 
import pandas  as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

KMeans.cl

sc = StandardScaler()
excelfile = "diabetes.csv"


headers = ["Pregnacy","Glucose","Blood-Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function",
           "Age","Outcome"]

df = pd.read_csv(excelfile,names=headers)
x = pd.DataFrame()