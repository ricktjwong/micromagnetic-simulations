# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 23:06:40 2019

@author: Daniel
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./mumax/table_double_y.txt", delimiter="\t", header=None)

data_mx = np.array(data[2][1:]).astype(np.float)
data_Bx = np.array(data[5][1:]).astype(np.float)

plt.figure(figsize = (8,8))
plt.plot(data_Bx, data_mx)
plt.plot(data_Bx[1000:], data_mx[1000:])
plt.show()

