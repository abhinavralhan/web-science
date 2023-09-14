# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:08:43 2021

@author: Vishal Vidhani
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure

df = pd.read_csv(r'LinkInformation.csv')

figure(figsize=(10, 8))
sns.histplot(df.URLfragments, color = "skyblue", ec="black")
plt.ylabel('Per Page')
plt.xlabel('URLfragments')
plt.title('Histogram of URLfragments per page')

figure(figsize=(10, 8))
sns.histplot(df.INTcount, color = "orange", ec="black")
plt.ylabel('Per Page')
plt.xlabel('INTcount')
plt.title('Histogram of INTcount per page')

figure(figsize=(10, 8))
sns.histplot(df.EXTcount, color = "pink", ec="black")
plt.ylabel('Per Page')
plt.xlabel('EXTcount')
plt.title('Histogram of EXTcount per page')