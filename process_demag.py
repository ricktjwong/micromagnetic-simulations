import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('./single/rect_single_cobalt.txt')
rows = []
for i in range(140):
    rows.append(data[40*i : 40*(i+1)])
print(len(rows))
rows = np.array(rows)
print(rows)
# plt.scatter(rows[:,0], rows[:,1])
# plt.show()



# cellsize = 5e-9
# x = [cellsize * i for i in range(40)]
# print(len(data[:,0]))
# print(len(data[:,1]))
# print(len(data[:,2]))