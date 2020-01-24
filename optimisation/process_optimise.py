import numpy as np
import matplotlib.pyplot as plt

costs = np.load('./sim_annealing/test_run/costs0.002417851639229262.npy')
actions = np.load('./sim_annealing/test_run/action0.002417851639229262.npy')
print(actions[-1])
plt.scatter([i+1 for i in range(len(costs))], costs, c='black', marker='x')
plt.show()
