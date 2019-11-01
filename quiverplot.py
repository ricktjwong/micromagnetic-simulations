import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('seaborn-bright')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['lines.linewidth'] = 1
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'


def plot_3D(n: int):
    # Convert from A/m to T (1 A/m -> 0.000001254 T)
    data = np.array(np.loadtxt('./single/rect_single_cobalt.txt')) / 10000

    # The order here is u, v, w = (40, 140, 24)
    data_field = data.reshape(40, 140, 24, 3, order="F")

    Y, X, Z = np.meshgrid(np.arange(0, 140, 1),
                        np.arange(0, 40, 1),
                        np.arange(0, 24, 1))

    # sample every 5th
    X, Y, Z = X[::n, ::n, ::n], Y[::n, ::n, ::n], Z[::n, ::n, ::n]
    u, v, w = data_field[:, :, :, 0], data_field[:, :, :, 1], data_field[:, :, :, 2]
    u, v, w = u[::n, ::n, ::n], v[::n, ::n, ::n], w[::n, ::n, ::n]

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.quiver(X, Y, Z, u, v, w, length=0.1)
    plt.show()


def plot_2D_quiver(file_path: str, zslice: int):
    x,y,z, _,_,_ = get_meta_data(file_path)
    data = np.array(np.loadtxt(file_path))
    data_field = data.reshape(x, y, z, 3, order="F")
    u, v, w = data_field[:,:,:,0], data_field[:,:,:,1], data_field[:,:,:,2]
    mag = (u * u + v * v + w * w) ** 0.5
    mag_slice = mag[:,:,zslice]
    Y, X = np.meshgrid(np.arange(0, y, 1), np.arange(0, x, 1))
    fig, ax = plt.subplots()
    # Choose a z slice
    ax.quiver(X, Y, u[:,:,zslice], v[:,:,zslice], 1)
    CS = ax.contour(X, Y, mag_slice, 12, linewidths=[1])
    ax.clabel(CS, inline=1, fontsize=8)
    ax.set_aspect('equal')
    # rect1 = patches.Rectangle((10, 30), 20, 120, linewidth=1, edgecolor='r', facecolor='none')
    # rect2 = patches.Rectangle((70, 30), 24, 120, linewidth=1, edgecolor='r', facecolor='none')
    # ax.add_patch(rect1)
    # ax.add_patch(rect2)
    plt.savefig(file_path.split('/')[-1].split('.')[0] + '.pdf', dpi=1000)
    plt.show()


def plot_2D_stream(z: int):
    data = np.array(np.loadtxt('./single/rect_single_cobalt.txt'))
    data_field = data.reshape(40, 140, 24, 3, order="F")
    u, v = data_field[:, :, :, 0], data_field[:, :, :, 1]
    Y, X = np.meshgrid(np.arange(0, 140, 1),
                       np.arange(0, 40, 1))
    fig, ax = plt.subplots(figsize=(7,2))
    # Choose a z slice
    ax.streamplot(Y, X, v[:,:,z], u[:,:,z])
    ax.set_aspect('equal')
    plt.show()


def get_meta_data(file_path: str):
    headers = {}
    with open(file_path) as f:
        for line in f:
            if line[0] != '#': break
            key_value = line.split('# ')[1].split(':')
            key, value = key_value[0], key_value[1].split('\n')[0].strip()
            headers[key] = value
    return int(headers['xnodes']), int(headers['ynodes']), int(headers['znodes']), \
           float(headers['xstepsize']), float(headers['ystepsize']), float(headers['zstepsize'])


# plot_3D(5)
# plot_2D_quiver(file_path="./data/stray_field/processed/double_100_x_120/strayfield_updown_doubleAsym_100_200_120.ovf", zslice=0)
# plot_2D_quiver(file_path="./data/stray_field/processed/two_rows/strayfield_2rows_100_100_100.ovf", zslice=0)
# plot_2D_quiver(file_path="./data/stray_field/processed/two_rows/strayfield_2rows_100_150_100.ovf", zslice=0)

# plot_2D_quiver(file_path="./data/stray_field/processed/permalloy_6array.txt", zslice=0)
# plot_2D_quiver(file_path="./data/stray_field/processed/strayfield_updown_6array_100_200_120.ovf", zslice=0)

# plot_2D_quiver(file_path="./data/stray_field/processed/two_rows/strayfield_2rows_100_200_100.ovf", zslice=0)
# plot_2D_quiver(file_path="./data/stray_field/processed/two_rows/strayfield_2rows_staggered_100_200_100.ovf", zslice=0)
# plot_2D_quiver(file_path="./data/stray_field/processed/two_rows/strayfield_2rows_staggered_100_150_100.ovf", zslice=0)
plot_2D_quiver(file_path="./data/stray_field/processed/two_rows/strayfield_2rows_staggered_100_200_100.ovf", zslice=0)

# plot_2D_stream(0)
