# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 23:06:40 2019

@author: Daniel
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


data = np.array(np.loadtxt('./single/rect_single_cobalt.txt'))/10000
data_field = data.reshape(40,140,24,3, order = "F") # the order here is x,y,z = (40,140,24)

x, y, z = np.meshgrid(np.arange(0, 140, 1), # but the order here is (140,40,24) to match array dimensions ??
                      np.arange(0, 40, 1),
                      np.arange(0, 24, 1))

x,y,z = x[::5,::5,::5], y[::5,::5,::5], z[::5,::5,::5] # sample every 5th

test = np.array([[1,2,3],[4,5,6]])
a,b,c = test[:,0], test[:,1], test[:,2]

u,v,w = data_field[:,:,:,0], data_field[:,:,:,1], data_field[:,:,:,2]
u,v,w = u[::5,::5,::5], v[::5,::5,::5], w[::5,::5,::5]

fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.quiver(y,x,z,u,v,w, length=0.1) # y,x,z axis seems to be the most correct ??
plt.show()
