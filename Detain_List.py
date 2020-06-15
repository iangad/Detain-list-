# -*- coding: utf-8 -*-
"""

# Upload the desired file.
name the file as "**r.csv**" and upload it
"""

import pandas as pd
from google.colab import files
uploaded = files.upload()

"""# Specified file converted to dataframe"""

import io                                              
import random
df2 = pd.read_csv(io.BytesIO(uploaded['r.csv']),encoding= 'unicode_escape')
df2.dropna(inplace=True)
df2.replace(' ---',round(random.uniform(75,100),2),inplace=True)
df2.head()

"""# Filtering out the students with less than 75% attendance"""

# df2.shape[0]
# for i in range(4,32):
  # print(df2.columns[i],end=" ")
import numpy as np
l=[]
for i in range(0,df2.shape[0]):
  for j in range(4,28):
    if float(df2.iloc[i].values[j])<75:
      if i not in l:
        l.append(i)

# print(l)

# df2.head()
# df2.describe()

"""# Creating the data frame of the less than 75% attendance students"""

# print(df2.columns[0])
li=[]
make= pd.DataFrame()
for j in range(df2.shape[1]):
  for i in range(df2.shape[0]):
    if i in l:
      li.append(df2.iloc[i].values[j])
  make[df2.columns[j]]=li
  li.clear()
make.head()

"""# Filtering out the students with more than 75% attendance and creating a seperate data frame for them"""

#for attendance above 75%
l.clear()
li.clear()
flag=0
for i in range(0,df2.shape[0]):
  for j in range(4,28):
    if float(df2.iloc[i].values[j])<75:
      flag = 1
      continue
  if flag == 0 :
    if i not in l:
      l.append(i)
  flag = 0 
# print(df2.columns[0])

li=[]
attendance_OK= pd.DataFrame()
for j in range(df2.shape[1]):
  for i in range(df2.shape[0]):
    if i in l:
      li.append(df2.iloc[i].values[j])
  attendance_OK[df2.columns[j]]=li
  li.clear()
#attendance_OK.head()

"""# Converting the required data frames to .csv format"""

make.to_csv('make.csv')
files.download("make.csv")
attendance_OK.to_csv('attendance_OK.csv')
files.download("attendance_OK.csv")
