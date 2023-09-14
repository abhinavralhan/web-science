#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt

with open('sample.txt', 'r') as df:
    df_contents = df.read()

    d1 = dict()
    for i in df_contents:
        if i in d1:
            d1[i] = d1[i] + 1
        else:
            d1[i] = 1

width = 0.06
characters = d1.keys()
frequencies = d1.values()
plt.bar(characters, frequencies)
plt.xlabel('character distribution')
plt.ylabel('frequencies')
plt.title('Frequency Distribution Plot')
plt.show()
