import numpy as np
import matplotlib.pyplot as plt

# costs = np.load('./data/6x6/costs1.1417981541647708e-05.npy')
# actions = np.load('./data/6x6/action1.1417981541647708e-05.npy')
costs = np.load('./data/2x6/costs00019342813113834097.npy')
actions = np.load('./data/2x6/action00019342813113834097.npy')
print(actions[-1])
plt.scatter([i+1 for i in range(len(costs))], costs, c='black', marker='x')
plt.show()
