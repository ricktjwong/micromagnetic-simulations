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


def plot_2D_quiver_2(z: int):
    data = np.array(np.loadtxt('./data/stray_field/processed/permalloy_6array.txt'))
    data_field = data.reshape(200, 200, 12, 3, order="F")
    u, v, w = data_field[:,:,:,0], data_field[:,:,:,1], data_field[:,:,:,2]
    mag = (u * u + v * v + w * w) ** 0.5
    mag_slice = mag[:,:,z]
    Y, X = np.meshgrid(np.arange(0, 200, 1), np.arange(0, 200, 1))
    fig, ax = plt.subplots()
    # Choose a z slice
    ax.quiver(X, Y, u[:,:,z], v[:,:,z], 1)
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

# plot_3D(5)
# plot_2D_quiver(0)
plot_2D_quiver_2(0)
# plot_2D_stream(0)
