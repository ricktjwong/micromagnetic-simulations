import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['lines.linewidth'] = 1
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
    return int(headers['xnodes']), int(headers['ynodes']), int(headers['znodes']), \
           float(headers['xstepsize']), float(headers['ystepsize']), float(headers['zstepsize'])


def plot_strayfield(file_path: str, mag_dir: str):
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
    yrange = np.linspace(160, 179, 5, dtype = int)
    print(yrange)
    for i in yrange:
        mag_slice = mag[:, i, zslice]
        plt.plot([i for i in range(x)], mag_slice, label=str((i - 160) * 5)+'nm')
    plt.legend()
    # plt.savefig(file_path.split('/')[-1].split('.')[0] + '.pdf', dpi=1000)
    plt.show()


def plot_strayfield_compare(file_path: str, mag_dir: str, t: int):
    x, y, z, _, _, _ = get_meta_data(file_path)
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
    yslice = 190
    mag_slice = mag[:, yslice, zslice]
    plt.plot([i * 5 for i in range(x)], mag_slice, label=str(t/100))
    plt.legend()    

# plot_strayfield(file_path="./data/stray_field/rounded/strayfield_double_rounded_tip_100_100_100.ovf", mag_dir='y')

def compare_strayfields(base_path: str, thicknesses: [int], mag_dir: str):
    thicknesses = [10 * i for i in range(6, 13, 1)]
    for t in thicknesses:
        file_path = base_path + str(t) + ".ovf"
        plot_strayfield_compare(file_path=file_path, mag_dir=mag_dir, t=t)
    plt.savefig(file_path.split('/')[-1].split('.')[0] + '.pdf', dpi=1000)
    plt.show()

t = [10 * i for i in range(6, 13, 1)]
compare_strayfields(base_path="./data/stray_field/rect/single_600-100-z/strayfield_cobalt_single_rect_thickness_", thicknesses=t, mag_dir='y')
