import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'


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


def plot_strayfield(file_path: str, mag_dir: str, yslice: [int], dotted=False):
    x, y, z, _, _, _ = get_meta_data(file_path)
    print(x, y, z)
    zslice = int(z / 2)
    data = np.array(np.loadtxt(file_path))
    data_field = data.reshape(x, y, z, 3, order="F")
    u, v, w = data_field[:, :, :, 0], data_field[:, :, :, 1], \
        data_field[:, :, :, 2]
    if (mag_dir == 'x'):
        mag = u
        c = 'tab:blue'
    elif (mag_dir == 'y'):
        mag = v
        c = 'tab:orange'
    elif (mag_dir == 'z'):
        mag = w
        c = 'tab:green'
    elif (mag_dir == 'total'):
        mag = (u * u + v * v + w * w) ** 0.5
        c = 'tab:green'
    for i in yslice:
        mag_slice = mag[:, i, zslice]
        if dotted:
            plt.plot([i * 5 for i in range(x)],
                     mag_slice, label=str(i * 5) + 'nm',
                     linestyle='dashed',
                     c=c)
        else:
            plt.plot([i * 5 for i in range(x)],
                     mag_slice,
                     label=str(i * 5) + 'nm',
                     c=c)
    print(max(mag[int(x/3):int(x/3)*2, int(y/2), int(z/2)]))
    print(max(mag_slice))
    # plt.legend()
    # plt.savefig(file_path.split('/')[-1].split('.')[0] + '.pdf', dpi=1000)
    # plt.show()


def plot_strayfield_decay(file_path: str, mag_dir: str, xslice: [int]):
    x, y, z, _, _, _ = get_meta_data(file_path)
    print(x, y, z)
    zslice = int(z / 2)
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
    for i in xslice:
        mag_slice = mag[i, :, zslice]
        # plt.plot([i * 5 for i in range(x)], mag_slice, label=mag_dir)
        plt.plot([i * 5 for i in range(y)], mag_slice, label=str(i * 5) + 'nm')


def plot_strayfield_compare(file_path: str, mag_dir: str, yslice: [int], idx):
    x, y, z, _, _, _ = get_meta_data(file_path)
    print(x, y, z)
    zslice = int(z / 2)
    data = np.array(np.loadtxt(file_path))
    data_field = data.reshape(x, y, z, 3, order="F")
    u, v, w = data_field[:,:,:,0], data_field[:,:,:,1], data_field[:,:,:,2]
    if (mag_dir == 'x'):
        mag = u
    elif (mag_dir == 'y'):
        mag = v
    elif (mag_dir == 'z'):
        mag = w
    elif (mag_dir == 'total'):
        mag = (u * u + v * v + w * w) ** 0.5
    for i in yslice:
        mag_slice = mag[:, i, zslice]
        plt.plot([i * 5 for i in range(x)], mag_slice, label=str(10*idx + 60) + 'nm')
    plt.legend()


def extract_maxfield(file_path: str, yslice: int):
    x, y, z, _, _, _ = get_meta_data(file_path)
    print(x, y, z)
    zslice = int(z / 2)
    data = np.array(np.loadtxt(file_path))
    data_field = data.reshape(x, y, z, 3, order="F")
    u, v, w = data_field[:, :, :, 0], data_field[:, :, :, 1], \
        data_field[:, :, :, 2]
    mag = (u * u + v * v + w * w) ** 0.5
    u_max = max(u[:, yslice, zslice])
    v_max = max(v[:, yslice, zslice])
    w_max = max(w[:, yslice, zslice])
    mag_max = max(mag[:, yslice, zslice])
    return [u_max, v_max, w_max, mag_max]
