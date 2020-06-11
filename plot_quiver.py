import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as patches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 18
plt.rcParams['lines.linewidth'] = 2
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


def plot_2D_quiver(file_path: str, mag_dir: str):
    contours = np.linspace(-0.1, 0.1, 6)  # [0.01 * i for i in range(10)]
    x, y, z, _, _, _ = get_meta_data(file_path)
    zslice = int(z / 2)
    print(x, y, z)
    data = np.array(np.loadtxt(file_path))
    data_field = data.reshape(x, y, z, 3, order="F")
    u, v, w = data_field[:, :, :, 0], data_field[:, :, :, 1], \
        data_field[:, :, :, 2]
    if (mag_dir == 'x'):
        mag = u
    elif (mag_dir == 'y'):
        mag = v
    elif (mag_dir == 'z'):
        mag = w
    elif (mag_dir == 'total'):
        mag = (u * u + v * v + w * w) ** 0.5
    mag_slice = mag[:, :, zslice]
    Y, X = np.meshgrid(np.arange(0, y, 1), np.arange(0, x, 1))
    fig, ax = plt.subplots()
    # Choose a z slice
    skip = (slice(None, None, 5), slice(None, None, 5))
    ax.quiver(X[skip]*5, Y[skip]*5, u[:, :, zslice][skip],
              v[:, :, zslice][skip], 10, cmap='binary')
    repeat_y = np.repeat(mag_slice, 5, axis=0)
    repeat_x = np.repeat(repeat_y, 5, axis=1)
    if mag_dir == 'x':
        cmap = 'PiYG'
    else:
        cmap = 'seismic'
    im = ax.imshow(np.transpose(repeat_x), cmap=cmap,
                   vmin=-0.2, vmax=0.2, origin='lower')
    CS = ax.contour(X*5, Y*5, mag_slice, contours, linewidths=1)
    ax.clabel(CS, inline=1, fontsize=12)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.xlabel('$T$', labelpad=20)
    plt.colorbar(im, cax=cax)
    # ax.set_xlim([200, 820])
    # ax.set_ylim([180, 350])
    # ax.set_aspect('equal')
    # plt.savefig(file_path.split('/')[-1].split('.')[0] + '_B'
    #             + mag_dir + '.pdf', dpi=1000)
    plt.show()


def plot_2D_stream(z: int):
    data = np.array(np.loadtxt('./single/rect_single_cobalt.txt'))
    data_field = data.reshape(40, 140, 24, 3, order="F")
    u, v = data_field[:, :, :, 0], data_field[:, :, :, 1]
    Y, X = np.meshgrid(np.arange(0, 140, 1),
                       np.arange(0, 40, 1))
    fig, ax = plt.subplots(figsize=(7, 2))
    # Choose a z slice
    ax.streamplot(Y, X, v[:, :, z], u[:, :, z])
    ax.set_aspect('equal')
    plt.show()


def get_meta_data(file_path: str):
    headers = {}
    with open(file_path) as f:
        for line in f:
            if line[0] != '#': break
            if ':' in line:
                key_value = line.split('# ')[1].split(':')
                key, value = key_value[0], key_value[1].split('\n')[0].strip()
                headers[key] = value
    return int(headers['xnodes']), int(headers['ynodes']), \
        int(headers['znodes']), float(headers['xstepsize']), \
        float(headers['ystepsize']), float(headers['zstepsize'])
