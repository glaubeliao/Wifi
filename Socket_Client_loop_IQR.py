#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


HOST = '192.168.100.123'
PORT = 7000
data=[]
Output=[]
index=[]

for i in range (500):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    outdata = 'hello tcp'
    s.send(outdata.encode())
    indata = s.recv(1024)
    voc=float(indata[5:26])*1000
    index.append(i)
    data.append(voc)
    
s.close()

#-----------------------------------------------------------------------
df=pd.DataFrame(data)
df=df.set_axis(['voltage'], axis=1, inplace=False)
Q1 = np.percentile(df['voltage'], 25,interpolation = 'midpoint')
Q3 = np.percentile(df['voltage'], 75,interpolation = 'midpoint')
IQR = Q3 - Q1
print(IQR)
print("Old Shape: ", df.shape)
# Upper bound
upper = np.where(df['voltage'] >= (Q3+IQR))
# Lower bound
lower = np.where(df['voltage'] <= (Q1-IQR))
 
''' Removing the Outliers '''
df.drop(upper[0], inplace = True)
df.drop(lower[0], inplace = True)
df.to_excel('Air.xlsx') 
print("New Shape: ", df.shape)
#-----------------------------------------------------------------------

average = sum(data[100:499])/len(data[100:499])
print(average)
print(df['voltage'].mean(axis=0))

# Labeland Title
plt.xlabel("points", fontsize=20)
plt.xticks(fontsize=10)
plt.ylabel("mV", fontsize=20)
plt.yticks(fontsize=10)
plt.plot(index,data)
plt.plot(df)
plt.show()
