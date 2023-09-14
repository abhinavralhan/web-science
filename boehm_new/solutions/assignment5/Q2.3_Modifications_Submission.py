# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:07:04 2021

@author: Vishal Vidhani
"""

import pandas as pd
import seaborn as sns

#readinf making a copy of the csv file
df = pd.read_csv('LinkInformation.csv')
df_using = df.copy()

#cleaning the data 
df_using = df_using.mask(df_using.eq('None')).dropna()


df_using['formatted_time'] = pd.to_datetime(df_using.TimeStamp)
df_using['hours'] = df_using['formatted_time'].dt.hour

#making ranges 
df_using["ranges"] = pd.cut(df_using.PageCount, 7, right=False)
#making ranges into whole numbers
_, edges = pd.cut(df_using.PageCount, bins=7, retbins=True)
labels = [f'({abs(edges[i]):.0f}, {edges[i+1]:.0f}]' for i in range(len(edges)-1)]
df_using['PageRanges'] = pd.cut(df_using.PageCount, bins=7, labels=labels)

#plotting the graph
sns.set(rc = {'figure.figsize':(15,8)})
sns.barplot(x= df_using.hours, y= df_using.PageRanges )



