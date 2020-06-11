import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as patches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14
plt.rcParams['lines.linewidth'] = 2
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'

# x = np.load('./data/sweep_data/8array_sweep_totalB.npy')
# plt.imshow(x.T, origin='lower')
# plt.show()

x = np.load('./data/sweep_data/halbach_sweeps.npy')
fig, ax = plt.subplots()
aspect = 1
centers = [240, 600, 40, 200]
dx, dy = 20, 20
extent = [centers[0]-dx/2, centers[1]+dx/2, centers[2]-dy/2, centers[3]+dy/2]
im = ax.imshow(x, origin='lower',
               extent=extent, aspect=aspect)
# plt.xticks(np.arange(centers[0], centers[1]+dx, dx))
plt.yticks(np.arange(centers[2], centers[3]+dy, dy))
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="10%", pad=0.3, aspect=9/19.*10)
# plt.xlabel('$B_y/B_x$', labelpad=20)
plt.colorbar(im, cax=cax)
plt.savefig('halbach_sweeps.pdf', dpi=1000)
plt.show()

# data = np.load('./data/sweep_data/8array_z100_sweeps.npy')
# u = np.array([i[:, 0] for i in data])
# v = np.array([i[:, 1] for i in data])
# w = np.array([i[:, 2] for i in data])
# B = np.array([i[:, 3] for i in data])
# fig, ax = plt.subplots()
# aspect = (30/9.) * (9/60.)
# centers = [20, 100, 20, 600]
# dx, dy = 10, 20
# extent = [centers[0]-dx/2, centers[1]+dx/2, centers[2]-dy/2, centers[3]+dy/2]
# im = ax.imshow((v / u).T, origin='lower', cmap='seismic', vmin=-1, vmax=3,
#                extent=extent, aspect=aspect)
# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="10%", pad=0.3, aspect=30/9.*10)
# # plt.xlabel('$B_y/B_x$', labelpad=20)
# plt.xticks(np.arange(centers[0], centers[1]+dx, dx))
# plt.yticks(np.arange(centers[3], centers[2]+dy, dy))
# plt.colorbar(im, cax=cax)
# # plt.savefig('8array_z20_sweeps_ByBx_ratio.pdf', dpi=1000)
# plt.show()

# data = np.load('./data/sweep_data/perm_single_z100.npy')
# x = [i for i in range(10, 610, 10)]
# u, v, w, B = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
# plt.scatter(x, v, marker='x', c='b', s=150)
# plt.ylim(-0.005, 0.035)
# data = np.load('./data/sweep_data/perm_single_z20.npy')
# x = [i for i in range(10, 610, 10)]
# u, v, w, B = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
# plt.scatter(x, v, marker='x', c='red', s=150)
# plt.ylim(-0.001, 0.012)
# plt.savefig('perm_single_z100.pdf', dpi=1000)
plt.show()
