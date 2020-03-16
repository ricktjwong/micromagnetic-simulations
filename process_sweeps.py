import numpy as np
import matplotlib.pyplot as plt

# x = np.load('./data/sweep_data/8array_sweep_totalB.npy')
# plt.imshow(x.T, origin='lower')
# plt.show()

# x = np.load('./data/sweep_data/halbach_sweeps.npy')
# plt.imshow(x, origin='lower', interpolation='gaussian')
# plt.show()

data = np.load('./data/sweep_data/8array_z20_sweeps.npy')
u = np.array([i[:, 0] for i in data])
v = np.array([i[:, 1] for i in data])
w = np.array([i[:, 2] for i in data])
B = np.array([i[:, 3] for i in data])
plt.imshow((v / u).T, origin='lower', vmin=0, vmax=2)
plt.show()
