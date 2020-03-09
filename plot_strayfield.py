import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

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


def plot_rashba(file_path: str, yslice: [int]):
    eff_m = 0.023
    x, y, z, _, _, _ = get_meta_data(file_path)
    print(x, y, z)
    zslice = int(z / 2)
    data = np.array(np.loadtxt(file_path))
    data_field = data.reshape(x, y, z, 3, order="F")
    u, v, w = data_field[:, :, :, 0], data_field[:, :, :, 1], data_field[:, :, :, 2]
    fig, ax1 = plt.subplots()
    # ax1.set_ylabel("alpha (eVm)")
    ax2 = ax1.twinx()
    # ax2.set_ylabel("Magnetic Field (T)")
    for i in yslice:
        Bx = u[:, i, zslice]
        By = v[:, i, zslice]
        B = (u*u + v*v + w*w) ** 0.5
        B = B[:, i, zslice]

        grad_B = np.gradient(B)
        grad_Bx = np.gradient(Bx)

        dphi_dx = (Bx * grad_B - B * grad_Bx)/(B*By*2*np.pi)  # asumes in nanometres
        # extra 2pi factor from X = 2(pi)x
        alpha = (3.818E-11/eff_m) * dphi_dx  # in eVm ## first factor hbar^2/2em, divide by e for eVs
        ax1.plot([i * 5 for i in range(x)], alpha, color="blue")  # label="α",
        ax2.plot([i * 5 for i in range(x)], Bx, color="brown")  # label= "$B_x$"
        ax2.plot([i * 5 for i in range(x)], By, color="green")  # label="$B_y$"
        ax2.plot([i * 5 for i in range(x)], B,  color="red")  # label="$|B|$"
        # plt.show()


# plot_strayfield('./data/stray_field/transverse_dw/strayfield1.ovf', mag_dir='y', yslice=[50])
# plot_strayfield('./optimisation/data/ovf/12x12_box_best.out/strayfield_optimise.ovf', mag_dir='total', yslice=[12])
# plot_strayfield('./data/stray_field/halbach_switching/switch_study_perm_100_60/halbach_switch_perm.4.out/strayfield5.ovf', mag_dir='y', yslice=[155])
# plot_strayfield('./data/stray_field/halbach_switching/halbach_ideal_100-60.out/strayfield.ovf', mag_dir='y', yslice=[155])
# plot_strayfield('./strayfield_2rows_6array_periodic.out/strayfield_6array_2rows_PBC_6eachside.ovf', mag_dir='y', yslice=[150])
# plot_strayfield('./optimisation/data/ovf/12x12_box_best_200_4.out/strayfield_optimise.ovf', mag_dir='total', yslice=[12])
# plot_strayfield('./halbach_periodic_hlength/halbach_periodic_hlength.0.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])
# plot_strayfield('./halbach_periodic_hlength/halbach_periodic_hlength.1.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])
# plot_strayfield('./halbach_periodic_hlength/halbach_periodic_hlength.2.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])
# plot_strayfield('./halbach_periodic_hlength/halbach_periodic_hlength.3.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])
# plot_strayfield('./halbach_periodic_hlength/halbach_periodic_hlength.4.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])
# plot_strayfield('./halbach_periodic_hlength/halbach_periodic_hlength.5.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])
# plot_strayfield('./halbach_periodic_hlength/halbach_periodic_hlength.6.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])

# plot_strayfield('./halbach_periodic_vwidth/halbach_periodic_vwidth.0.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])
# plot_strayfield('./halbach_periodic_vwidth/halbach_periodic_vwidth.1.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])
# plot_strayfield('./halbach_periodic_vwidth/halbach_periodic_vwidth.2.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])
# plot_strayfield('./halbach_periodic_vwidth/halbach_periodic_vwidth.3.out/strayfield_halbachPeriodic.ovf', mag_dir='y', yslice=[190])

# plot_strayfield(file_path='./data/stray_field/halbach_switching/switch_study_perm_100_60/halbach_switch_perm.4.out/strayfield5.ovf', mag_dir='total', yslice = [145,155,165])
# plot_strayfield(file_path='./data/stray_field/halbach_switching/switch_study_perm_100_60/halbach_switch_perm.4.out/strayfield5.ovf', mag_dir='x', yslice = [145,155,165])
# plot_strayfield(file_path='./data/stray_field/halbach_switching/switch_study_perm_100_60/halbach_switch_perm.4.out/strayfield5.ovf', mag_dir='y', yslice = [145,155,165])
plot_rashba(file_path='./data/stray_field/halbach_switching/switch_study_perm_100_60/halbach_switch_perm.4.out/strayfield5.ovf', yslice = [155])

plt.savefig('spin_orbit_alpha.pdf', dpi=1000)
plt.show()