import numpy as np
import matplotlib.pyplot as plt

costs = np.load('./data/costs00019342813113834097.npy')
actions = np.load('./data/action00019342813113834097.npy')
print(actions[-1])
plt.scatter([i+1 for i in range(len(costs))], costs, c='black', marker='x')
plt.show()
