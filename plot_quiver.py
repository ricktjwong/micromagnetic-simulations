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


def plot_2D_quiver(file_path: str, mag_dir: str, zslice: int):
    contours = [0.01 * i for i in range(10)]
    x, y, z, _, _, _ = get_meta_data(file_path)
    data = np.array(np.loadtxt(file_path))
    data_field = data.reshape(x, y, z, 3, order="F")
    u, v, w = data_field[:,:,:,0], data_field[:,:,:,1], data_field[:,:,:,2]
    if (mag_dir == 'x'):
        mag = abs(u)
    elif (mag_dir == 'y'):
        mag = abs(v)
    elif (mag_dir == 'z'):
        mag = abs(w)
    elif (mag_dir == 'total'):
        mag = (u * u + v * v + w * w) ** 0.5
    mag_slice = mag[:,:,zslice]
    Y, X = np.meshgrid(np.arange(0, y, 1), np.arange(0, x, 1))
    fig, ax = plt.subplots()
    # Choose a z slice
    ax.quiver(X, Y, u[:,:,zslice], v[:,:,zslice], 1)
    CS = ax.contour(X, Y, mag_slice, contours, linewidths=[1])
    ax.clabel(CS, inline=1, fontsize=8)
    ax.set_aspect('equal')
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
            if ':' in line:
                key_value = line.split('# ')[1].split(':')
                key, value = key_value[0], key_value[1].split('\n')[0].strip()
                headers[key] = value
    return int(headers['xnodes']), int(headers['ynodes']), int(headers['znodes']), \
           float(headers['xstepsize']), float(headers['ystepsize']), float(headers['zstepsize'])


# Double rect
# plot_2D_quiver(file_path="./data/stray_field/rect/double_100_x_120/strayfield_updown_doubleAsym_100_100_120.ovf", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/rect/double_100_x_120/strayfield_updown_doubleAsym_100_150_120.ovf", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/rect/double_100_x_120/strayfield_updown_doubleAsym_100_200_120.ovf", mag_dir='total', zslice=6)

# Six rects
# plot_2D_quiver(file_path="./data/stray_field/rect/permalloy_6array.txt", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/rect/strayfield_updown_6array_100_200_120.ovf", mag_dir='total', zslice=6)

# Two rows of three rects
# plot_2D_quiver(file_path="./data/stray_field/rect/two_rows/strayfield_2rows_100_100_100.ovf", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/rect/two_rows/strayfield_2rows_100_150_100.ovf", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/rect/two_rows/strayfield_2rows_100_200_100.ovf", mag_dir='total', zslice=6)

# Two rows of staggered rects
# plot_2D_quiver(file_path="./data/stray_field/rect/two_rows/strayfield_2rows_staggered_100_100_100.ovf", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/rect/two_rows/strayfield_2rows_staggered_100_150_100.ovf", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/rect/two_rows/strayfield_2rows_staggered_100_200_100.ovf", mag_dir='total', zslice=6)

# Hemisphere tips
# plot_2D_quiver(file_path="./data/stray_field/hemisphere/strayfield_one_hemisphere_tip.ovf", mag_dir='total', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/hemisphere/strayfield_double_hemisphere_tip_100_100_100.ovf", mag_dir='total', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/hemisphere/strayfield_double_hemisphere_tip_100_100_100_Co.ovf", mag_dir='total', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/hemisphere/strayfield_six_hemisphere_tip.ovf", mag_dir='total', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/hemisphere/strayfield_six_hemisphere_tip_Co.ovf", mag_dir='total', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/hemisphere/strayfield_one_conical_tip.ovf", mag_dir='total', zslice=0)

# Rounded tips
# plot_2D_quiver(file_path="./data/stray_field/rounded/strayfield_one_rounded_tip.ovf", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/rounded/strayfield_double_rounded_tip_100_100_100.ovf", mag_dir='x', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/rounded/strayfield_six_rounded_tip.ovf", mag_dir='total', zslice=6)

# Halbach array
# plot_2D_quiver(file_path="./data/stray_field/halbach/strayfield_halbach_600_120_100.ovf", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/halbach/strayfield_halbach_600_200_100.ovf", mag_dir='total', zslice=6)
# plot_2D_quiver(file_path="./data/stray_field/halbach/strayfield_halbach_600_300_100.ovf", mag_dir='total', zslice=6)

# Compare
plot_2D_quiver(file_path="./data/stray_field/compare_cobalt_double-100-600-100/strayfield_double_rect_100_100_100.ovf", mag_dir='total', zslice=10)
plot_2D_quiver(file_path="./data/stray_field/compare_cobalt_double-100-600-100/strayfield_double_rounded_tip_100_100_100.ovf", mag_dir='total', zslice=10)
