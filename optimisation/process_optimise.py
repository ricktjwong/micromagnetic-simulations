import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 1
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'

# costs = np.load('./data/2x6/costs00019342813113834097.npy')
# actions = np.load('./data/2x6/action00019342813113834097.npy')
# costs = np.load('./data/6x6/costs1.1417981541647708e-05.npy')
# actions = np.load('./data/6x6/action1.1417981541647708e-05.npy')
costs = np.load('./data/12x12/costs1.1417981541647708e-05.npy')
actions = np.load('./data/12x12/action1.1417981541647708e-05.npy')
# costs = np.load('./data/14x14/costs-combined.npy')
# actions = np.load('./data/14x14/action-combined.npy')
# costs = np.load('./data/6x6_box/costs1.1417981541647708e-05.npy')
# actions = np.load('./data/6x6_box/action1.1417981541647708e-05.npy')
# costs = np.load('./data/12x12_box/costs1.1417981541647708e-05.npy')
# actions = np.load('./data/12x12_box/action1.1417981541647708e-05.npy')
# costs = np.load('./data/12x12_box_200/costs1.1417981541647708e-05.npy')
# actions = np.load('./data/12x12_box_200/action1.1417981541647708e-05.npy')
# costs = np.load('./data/12x12_box_200_4/costs1.1417981541647708e-05.npy')
# actions = np.load('./data/12x12_box_200_4/action1.1417981541647708e-05.npy')
# costs = np.load('./data/12x12_200/costs1.1417981541647708e-05.npy')
# actions = np.load('./data/12x12_200/action1.1417981541647708e-05.npy')
print(costs[np.argmax(costs)])
print(actions[np.argmax(costs)])
print(actions[-1])
print(costs[-1])
plt.scatter([i+1 for i in range(len(costs))], costs, c='b', marker='x', s=150)
plt.savefig('cost_fn.pdf', dpi=1000)
plt.show()
