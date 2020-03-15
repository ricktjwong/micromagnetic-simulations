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
    # plt.figure()
    for i in yslice:
        mag_slice = mag[:, i, zslice]
        # plt.plot([i * 5 for i in range(x)], mag_slice, label=mag_dir)
        plt.plot([i * 5 for i in range(x)], mag_slice, label=str(i * 5) + 'nm')
    print(max(mag[int(x/3):int(x/3)*2, int(y/2), int(z/2)]))
    print(max(mag_slice))
    # plt.legend()
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


def extract_maxfield(file_path: str, mag_dir: str, yslice: int):
    x, y, z, _, _, _ = get_meta_data(file_path)
    print(x, y, z)
    zslice = int(z / 2)
    data = np.array(np.loadtxt(file_path))
    data_field = data.reshape(x, y, z, 3, order="F")
    u, v, w = data_field[:,:,:,0], data_field[:,:,:,1], data_field[:,:,:,2]
    mag = (u * u + v * v + w * w) ** 0.5
    u_max = u[:, yslice, zslice]
    v_max = v[:, yslice, zslice]
    w_max = w[:, yslice, zslice]
    mag_max = mag[:, yslice, zslice]
    return [u, v, w_max, mag_max]


# all_B = []
# for i in range(20, 110, 10):
#     b_row = []
#     for j in range(0, 19):
#         B = extract_maxfield(file_path='../halbach_sweep/halbach_vwidth_' + str(i) + '/halbach_sweep.' + str(j) + '.out/strayfield_halbachPeriodic.ovf', mag_dir='total', yslice=190)
#         b_row += [B]
#     all_B += [b_row]
# print(all_B)
# np.save('halbach_sweeps', all_B)


# plot_strayfield(file_path='./data/stray_field/halbach_switching/switch_study_perm_100_60/halbach_switch_perm.4.out/strayfield5.ovf', mag_dir='total', yslice = [145,155,165])
# plot_strayfield(file_path='./data/stray_field/halbach_switching/switch_study_perm_100_60/halbach_switch_perm.4.out/strayfield5.ovf', mag_dir='total', yslice = [145,155,165])
# plot_strayfield(file_path='./data/stray_field/halbach_switching/switch_study_perm_100_60/halbach_switch_perm.4.out/strayfield5.ovf', mag_dir='x', yslice = [145,155,165])
# plot_strayfield(file_path='./data/stray_field/halbach_switching/switch_study_perm_100_60/halbach_switch_perm.4.out/strayfield5.ovf', mag_dir='y', yslice = [145,155,165])
# plot_strayfield(file_path='./data/stray_field/360_dw/strayfield_360wall9.ovf', mag_dir='y', yslice=[56, 64, 74])

all_B = []
for i in range(20, 620, 20):
    b_row = []
    for j in range(0, 30):
        B = extract_maxfield(file_path='./8array_z100_sep_' + str(i) + '/8array.' + str(j) + '.out/strayfield.ovf', mag_dir='total', yslice=190)
        b_row += [B]
        print(B)
    all_B += [b_row]
    print(b_row)
print(all_B)
np.save('8array_z100_sweeps', all_B)

# plt.savefig('strayfield_antiparallel6_kjaergaard.pdf', dpi=1000)
# plt.show()
