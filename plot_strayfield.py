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


def plot_strayfield(file_path: str, mag_dir: str, yslice: [int]):
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
        # plt.plot([i * 5 for i in range(x)], mag_slice, label=mag_dir)
        plt.plot([i * 5 for i in range(x)], mag_slice, label=str(i * 5) + 'nm')
    print(max(mag_slice))
    plt.legend()
    # plt.savefig(file_path.split('/')[-1].split('.')[0] + '.pdf', dpi=1000)
    # plt.show()


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


def compare_strayfields(base_path: str, thicknesses: [int], mag_dir: str):
    thicknesses = [10 * i for i in range(6, 13, 1)]
    for t in thicknesses:
        file_path = base_path + str(t) + ".ovf"
        plot_strayfield_compare(file_path=file_path, mag_dir=mag_dir, t=t)
    plt.savefig(file_path.split('/')[-1].split('.')[0] + '.pdf', dpi=1000)
    plt.show()


# plot_strayfield('./data/stray_field/halbach_cylinder/strayfield_halbach_cylinder_4.ovf', 'y', [180])
# plot_strayfield('./data/stray_field/halbach_cylinder/strayfield_halbach_cylinder_control.ovf', 'y', [180])
# plot_strayfield('./data/stray_field/halbach_cylinder/strayfield_halbach_cylinder_8.ovf', 'y', [180])
# plot_strayfield('./data/stray_field/current_design/strayfield_halbach2rows_antiparallel.ovf', 'y', [150])
# plot_strayfield('./data/stray_field/cobalt_tworows_compare/strayfield_6array_2rows_PBC_6eachside.ovf', 'y', [150])

# plot_strayfield('./data/stray_field/halbach_cylinder/strayfield_halbach_cylinder_12.ovf', 'y', [200, 210, 220])
# plot_strayfield('./out.out/strayfield_optimise.ovf', 'total', [6])
# plt.savefig('strayfield_halbach_cylinder_12.pdf', dpi=1000)
# plt.show()
