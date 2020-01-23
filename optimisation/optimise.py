import os
import sys
import random
import numpy as np
import time


def run_mumax_script(filename: str):
    os.system('mumax3-cuda6.5 ./mumax_scripts/' + filename)


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


def initialise_gridspace(x0: [int], filename: str):
    configs = ['uniform(0, 0, 0)', 'uniform(0, 1, 0)', 'uniform(0, -1, 0)',
               'uniform(1, 0, 0)', 'uniform(-1, 0, 0)']
    with open('./boilerplate.mx3') as f:
        with open('./mumax_scripts/' + filename, 'w') as f1:
            for line in f:
                f1.write(line)
            lines = '\n'
            lines += 'm.SetRegion(1, uniform(0, 0, 0))\n'
            lines += 'm.SetRegion(2, uniform(0, 0, 0))\n'
            lines += 'm.SetRegion(3, uniform(0, 0, 0))\n'
            lines += 'm.SetRegion(4, uniform(0, 0, 0))\n'
            for i in range(len(x0)):
                lines += 'm.SetRegion(' + str(i + 5) + ', ' + configs[x0[i]] + ')\n'
            lines += 'relax()\n'
            lines += 'saveas(m, "m_optimise_' + filename.split('.')[0] + '")\n'
            lines += 'saveas(B_demag, "strayfield_optimise_' + filename.split('.')[0] + '")\n'
            f1.write(lines)


def find_max_B(file_path: str, yslice: int):
    x, y, z, _, _, _ = get_meta_data(file_path)
    zslice = int(z / 2)
    data = np.array(np.loadtxt(file_path))
    data_field = data.reshape(x, y, z, 3, order='F')
    u, v, w = data_field[:, :, :, 0], data_field[:, :, :, 1], data_field[:, :, :, 2]
    mag = (u * u + v * v + w * w) ** 0.5
    mag_slice = mag[:, yslice, zslice]
    return max(mag_slice)


def acceptance_probability(old, new, T):
    """
    If the new cost value is larger than the old one, accept the new cost
    value with 100% probability. If the new cost value is smaller than the old,
    accept the new cost value with a probability equal to exp[(new - old) / T]
    T gets smaller at every iteration, i.e. we accept bad cost values with
    lower probability
    """
    if new < old:
        a = 1
    else:
        a = np.exp((new - old) / T)
    return a


def simulated_annealing(x0, T, T_min, alpha):
    min_costs = []
    min_actions = []
    min_cost = 1000
    while T > T_min:
        count = 0
        while(count < 100):
            filename = str(random.randint(1111111111, 9999999999)) + '.mx3'
            initialise_gridspace(x0, filename)
            run_mumax_script(filename)
            while not os.path.exists('./mumax_scripts/strayfield_optimise_' + filename):
                time.sleep(20)
            cost_new = find_max_B(filename, 6)
            ep = acceptance_probability(min_cost, cost_new, T)
            if ep > random.random():
                min_cost = cost_new
                min_action = x0.copy()
                min_costs.append(min_cost)
                min_actions.append(min_action)
            idx = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            if x0[idx] <= 4:
                x0[idx] += 1
            count += 1
        np.save("sim_annealing/costs" + str(T), min_costs)
        np.save("sim_annealing/action" + str(T), min_actions)
        T = T * alpha


x0 = [0, 0, 0, 0, 0, 0, 0, 0]
T = 1.0
T_min = 0.00001
alpha = 0.8


# print(find_max_B('../out.out/strayfield_optimise.ovf', 6))
simulated_annealing(x0, T, T_min, alpha)
