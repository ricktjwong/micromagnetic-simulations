import numpy as np
import matplotlib.pyplot as plt

x = np.load('./data/sweep_data/8array_sweep_totalB.npy')
plt.imshow(x.T, origin='lower')
plt.show()
