import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-4, 4, 0.2)
y = np.arange(-4, 4, 0.2)

X, Y = np.meshgrid(x, y)
Ex = (X + 1)/((X+1) ** 2 + Y ** 2) - (X - 1)/((X-1) ** 2 + Y ** 2)
Ey = Y/((X+1) ** 2 + Y ** 2) - Y/((X-1) ** 2 + Y ** 2)

fig, ax = plt.subplots(figsize=(6,6))

ax.streamplot(X, Y, Ex, Ey)

ax.set_aspect('equal')
ax.plot(-1,0,'-or')
ax.plot(1,0,'-ob')
ax.set_title('Stream Plot of Two Point Charges')

plt.show()
