import pandas  as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.preprocessing import StandardScaler 
import sklearn.model_selection._split as sp 
count1 = 10
while count1 != 0:
  print(count1)
  count1 -= 1
print("We have liftoff!")

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

hairstyleslen = len(hairstyles)
pricesize = len(prices)
weeksize = len(last_week)
print(hairstyleslen)
total_price = 0
for i in prices:
  total_price +=i
average_price = total_price /pricesize
print("Average Haircut price:\n",average_price)
new_prices= [num - 5 for num in prices]
print(new_prices)
total_revenue = 0

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(F):
  C = (F -32)  * (5/9)
  print(C)

f_to_c(100)
def c_to_f(C):
  F = C * (9/5) +32
  print(F)
c_to_f(0)

def get_force(mass, acceleration):
  return mass*acceleration

train_force = get_force(train_mass,train_acceleration)
words = str(train_force)
print("The GE train supplies "+words+" Newtons of force")
def get_energy(mass,c=3*10**8):
  return mass**c
bomb_energy = get_energy(bomb_mass)
def get_work(mass,acceleration,distance):
  force =get_force(mass,acceleration)
  work = force * distance
  return work

train_work = get_work(train_mass,train_acceleration,train_distance)
print(train_work)
print(1)



for i in range(hairstyleslen):
  
  total_revenue += (prices[i] + last_week[i])
  i+=1
print("Total Revenue",total_revenue)
average_daily_revenue = total_revenue/7

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] <30]
print(cuts_under_30)