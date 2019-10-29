import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.1)
y = np.arange(-2, 2, 0.1)

X, Y = np.meshgrid(x, y)
u = np.cos(X)
v = np.sin(Y)

u = X/5
v = -Y/5

fig, ax = plt.subplots(figsize=(9,9))

print(X.shape)
print(Y.shape)
print(u.shape)
print(v.shape)

ax.quiver(X,Y,u,v)

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_aspect('equal')

plt.show()