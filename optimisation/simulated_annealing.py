import random
import numpy as np


def acceptance_probability(old, new, T):
    """
    If the new cost value is smaller than the old one, accept the new cost
    value with 100% probability. If the new cost value is large than the old,
    accept the new cost value with a probability equal to exp[-(new - old) / T]
    T gets smaller at every iteration, i.e. we accept bad cost values with
    lower probability
    """
    if new < old:
        a = 1
    else:
        a = np.exp((old - new) / T)
    return a


def simulate_annealing(x0, T, T_min, alpha):
    min_costs = []
    min_actions = []
    min_cost = 1000
    while T > T_min:
        count = 0
        while(count < 100):
            run_mumax_script()
            cost_new = evaluate_bfield(mumax_output_file)
            ep = acceptance_probability(min_cost, cost_new, T)
            if ep > random.random():
                min_cost = cost_new
                min_action = x0.copy()
                min_costs.append(min_cost)
                min_actions.append(min_action)
            idx = random.choice([0, 1, 2, 3])
            move = get_action(idx)
            x0[idx] += move
            count += 1
        np.save("sim_annealing/costs" + str(T), min_costs)
        np.save("sim_annealing/action" + str(T), min_actions)
        T = T * alpha


x0 = [0, 0, 0, 0, 0, 0, 0, 0]
T = 1.0
T_min = 0.00001
alpha = 0.8