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
    skip = (slice(None,None,5), slice(None,None,5))
    ax.quiver(X[skip]*5, Y[skip]*5, u[:,:,zslice][skip], v[:,:,zslice][skip], 10)
    CS = ax.contour(X*5, Y*5, mag_slice, contours, linewidths=[1])
    ax.clabel(CS, inline=1, fontsize=8)
    ax.set_aspect('equal')
    plt.savefig(file_path.split('/')[-1].split('.')[0] + '_By.pdf', dpi=1000)
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

# plot_2D_quiver(file_path="./data/stray_field/halbach_vary_width/vary_hlength/strayfield_halbachPeriodic_hlength_300.ovf", mag_dir='y', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/halbach_vary_width/vary_hlength/strayfield_halbachPeriodic_hlength_300_aligned.ovf", mag_dir='y', zslice=15)

# plot_2D_quiver(file_path="./data/stray_field/halbach_vary_width/vary_vwidth/strayfield_halbachPeriodic_vwidth_100.ovf", mag_dir='y', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/halbach_vary_width/vary_vwidth/strayfield_halbachPeriodic_vwidth_100_aligned.ovf", mag_dir='y', zslice=15)

# plot_2D_quiver(file_path="./data/stray_field/halbach_vary_width/vary_vwidth/strayfield_halbachPeriodic_vwidth_150.ovf", mag_dir='y', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/halbach_vary_width/vary_vwidth/strayfield_halbachPeriodic_vwidth_150_aligned.ovf", mag_dir='y', zslice=15)

# plot_2D_quiver(file_path="./data/stray_field/halbach_vary_width/vary_vwidth/strayfield_halbachPeriodic_vwidth_200.ovf", mag_dir='y', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/halbach_vary_width/vary_vwidth/strayfield_halbachPeriodic_vwidth_200_aligned.ovf", mag_dir='y', zslice=15)

# plot_2D_quiver(file_path="./data/stray_field/current_design/strayfield_halbach2rows_antiparallel.ovf", mag_dir='y', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/current_design/strayfield_halbach2rows_parallel.ovf", mag_dir='y', zslice=15)

# plot_2D_quiver(file_path="./data/stray_field/cobalt_tworows_compare/strayfield_rect_6array_2rows_noPBC.ovf", mag_dir='y', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/cobalt_tworows_compare/strayfield_rect_7array_2rows_noPBC.ovf", mag_dir='y', zslice=15)

# plot_2D_quiver(file_path="./cobalt-halbach-2rows/halbach2rows.0.out/m000000.ovf", mag_dir='y', zslice=15)
# plot_2D_quiver(file_path="./cobalt-halbach-2rows/halbach2rows.0.out/m000000.ovf", mag_dir='y', zslice=15)

# plot_2D_quiver(file_path="./data/stray_field/halbach_cylinder/strayfield_halbach_cylinder_4.ovf", mag_dir='total', zslice=10)
# plot_2D_quiver(file_path="./data/stray_field/halbach_cylinder/m_halbach_cylinder_8.ovf", mag_dir='total', zslice=10)

# plot_2D_quiver(file_path="./data/stray_field/cobalt_double-z-100/strayfield_double_rect_100_100_100.ovf", mag_dir='total', zslice=10)
# plot_2D_quiver(file_path="./data/stray_field/cobalt_double-z-100/strayfield_double_rounded_tip_100_100_100.ovf", mag_dir='total', zslice=10)

# plot_2D_quiver(file_path="./data/stray_field/current_design/strayfield_halbach2rows_antiparallel.ovf", mag_dir='total', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/cobalt_tworows_compare/strayfield_6array_2rows_PBC_6eachside.ovf", mag_dir='total', zslice=15)
# plot_2D_quiver(file_path="./data/stray_field/halbach_cylinder/strayfield_halbach_cylinder_12.ovf", mag_dir='total', zslice=15)
plot_2D_quiver(file_path="./data/stray_field/halbach_cylinder/modified_cyl.ovf", mag_dir='total', zslice=15)
