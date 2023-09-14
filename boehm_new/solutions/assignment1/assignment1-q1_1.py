#!/usr/bin/env python
# coding: utf-8

import random
import numpy as np
import matplotlib.pyplot as plt

i = 0
SIN = []
COSINE = []
X = []
while i < 10:
    i+=1
    randomNumber = random.randint(0,80)
    X.append(randomNumber)
    SIN.append(np.sin(randomNumber))
    COSINE.append(np.cos(randomNumber))

plt.plot(X, SIN, X, COSINE)
plt.xlabel('x random Value from 0 to 80')
plt.ylabel('sin(x) and cos(x)')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()
