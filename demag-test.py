import matplotlib

print(matplotlib.matplotlib_fname())

import matplotlib.pyplot as plt
import discretisedfield as df
import oommfc as oc

mesh = oc.Mesh(p1=(-100e-9, -100e-9, -100e-9), p2=(100e-9, 100e-9, 100e-9), cell=(5e-9, 5e-9, 5e-9))

def norm_fun(pos):
    x, y, z = pos
    if -50e-9 <= x <= 50e-9 and -50e-9 <= y <= 50e-9 and -50e-9 <= z <= 50e-9:
        return 8e5
    else:
        return 0

system = oc.System(name='airbox_method')
system.hamiltonian = oc.Exchange(A=1e-12) + oc.Demag()
system.dynamics = oc.Precession(gamma=oc.consts.gamma0) + oc.Damping(alpha=1)
system.m = df.Field(mesh, value=(0, 0, 1), norm=norm_fun)
system.m.norm.plane('z').mpl()

md=oc.MinDriver()
md.drive(system)

system.m.plane('z').mpl(figsize=(10, 10))

stray_field = system.hamiltonian.demag.effective_field


# x = [1,2,3]
# y = [2,4,6]
# plt.scatter(x, y)
# plt.show()
