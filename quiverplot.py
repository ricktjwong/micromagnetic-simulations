import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot_3D(n: int):
    # Convert from A/m to mT (1 A/m -> 0.000001254 T)
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


def plot_2D_quiver(z: int):
    data = np.array(np.loadtxt('./data/stray_field/processed/rect_single_cobalt.txt')) * 0.001254
    data_field = data.reshape(40, 140, 24, 3, order="F")
    u, v, w = data_field[:,:,:,0], data_field[:,:,:,1], data_field[:,:,:,2]
    mag = (u * u + v * v + w * w) ** 0.5
    mag_slice = mag[:,:,z]
    Y, X = np.meshgrid(np.arange(0, 140, 1), np.arange(0, 40, 1))
    fig, ax = plt.subplots()
    # Choose a z slice
    ax.quiver(X, Y, u[:,:,z], v[:,:,z], 1)
    CS = ax.contour(X, Y, mag_slice)
    ax.clabel(CS, inline=1, fontsize=10)
    ax.set_aspect('equal')
    # plt.savefig('single.png', dpi=1000)
    plt.show()


def plot_2D_quiver_2(file, ovf_format, zslice: int):
    x,y,z, _,_,_ = get_xyz_nodes(file, ovf_format)
    data = np.array(np.loadtxt(file))
    data_field = data.reshape(x, y, z, 3, order="F")
    u, v, w = data_field[:,:,:,0], data_field[:,:,:,1], data_field[:,:,:,2]
    mag = (u * u + v * v + w * w) ** 0.5
    mag_slice = mag[:,:,zslice]
    Y, X = np.meshgrid(np.arange(0, y, 1), np.arange(0, x, 1))
    fig, ax = plt.subplots()
    # Choose a z slice
    ax.quiver(X, Y, u[:,:,zslice], v[:,:,zslice], 1)
    CS = ax.contour(X, Y, mag_slice)
    ax.clabel(CS, inline=1, fontsize=10)
    ax.set_aspect('equal')
    # plt.savefig('single.png', dpi=1000)
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

def get_xyz_nodes(file, ovf_format):
    with open(file) as current_file:
        if ovf_format == "mumax_v1" :
            for i, line in enumerate(current_file):
                if i == 11:
                    x_step = float(line[13:])
                if i == 12:
                    y_step = float(line[13:])
                if i == 13:
                    z_step = float(line[13:])
                    
                if i == 20:
                    x_nodes = int(float(line[10:]))
                if i == 21:
                    y_nodes = int(float(line[10:]))
                if i == 22:
                    z_nodes = int(float(line[10:]))
                
                if i > 23:
                    break
                
        if ovf_format == "mumax_v2" :
            for i, line in enumerate(current_file):
                if i == 23:
                    x_step = float(line[13:])
                if i == 24:
                    y_step = float(line[13:])
                if i == 25:
                    z_step = float(line[13:])
                    
                if i == 20:
                    x_nodes = int(float(line[10:]))
                if i == 21:
                    y_nodes = int(float(line[10:]))
                if i == 22:
                    z_nodes = int(float(line[10:]))
                
                if i > 26:
                    break
        
        elif ovf_format == "oommf" :
            for i, line in enumerate(current_file):
                if i == 11:
                    x_step = float(line[13:])
                if i == 12:
                    y_step = float(line[13:])
                if i == 13:
                    z_step = float(line[13:])
                
                if i == 14:
                    x_nodes = int(float(line[10:]))
                if i == 15:
                    y_nodes = int(float(line[10:]))
                if i == 16:
                    z_nodes = int(float(line[10:]))
                    
                if i > 17:
                    break
            
    return x_nodes, y_nodes, z_nodes, x_step, y_step, z_step
"
# plot_3D(5)
# plot_2D_quiver(0)
plot_2D_quiver_2(file = "../data/stray_field/processed/test_ovf1text.ovf", ovf_format = "mumax_v1", zslice = 0)
# plot_2D_stream(0)


