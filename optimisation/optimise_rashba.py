import os
import random
import numpy as np
import matplotlib.pyplot as plt


def calculate_rashba(x0):
    Bx = x0[:, 0]
    By = x0[:, 1]
    eff_m = 0.014
    B = (Bx*Bx + By*By) ** 0.5
    grad_B = np.gradient(B)
    grad_Bx = np.gradient(Bx)
    dphi_dx = -(Bx*grad_B - B*grad_Bx) / (B*By*2*np.pi)
    alpha = (3.818E-11/eff_m) * dphi_dx
    cost = np.nanmax(alpha[alpha != np.inf])
    return cost


def acceptance_probability(old, new, T):
    """
    If the new cost value is larger than the old one, accept the new cost
    value with 100% probability. If the new cost value is smaller than the old,
    accept the new cost value with a probability equal to exp[(new - old) / T]
    T gets smaller at every iteration, i.e. we accept weaker cost values with
    lower probability
    """
    if new > old:
        a = 1
    else:
        a = np.exp((new - old) / T)
    return a


def simulated_annealing(x0: [float], T: float,
                        T_min: float, alpha: float):
    if not os.path.exists('./sim_annealing'):
        os.makedirs('sim_annealing')
    max_costs = []
    max_actions = []
    max_cost = 0.0
    x_new = x0.copy()
    while T > T_min:
        count = 0
        while(count < 200):
            cost_new = calculate_rashba(x_new)
            print('x0: ', x0)
            print('x_new: ', x_new)
            print('new cost: ' + str(cost_new))
            ap = acceptance_probability(max_cost, cost_new, T)
            if ap > random.random():
                x0 = x_new.copy()
                max_cost = cost_new
                max_costs.append(max_cost)
                max_actions.append(x0)
            # Choose Bx or By
            B_param = random.choice([0, 1])
            # Choose a parameter to change
            param = random.choice([i for i in range(20)])
            # Reset x_new to the latest accepted action
            x_new = x0.copy()
            # Make a move and make sure it is different from original
            new_move = random.choice([0.01, -0.01])
            x_new[param][B_param] += new_move
            count += 1
            print('max cost: ' + str(max_cost))
        np.save("sim_annealing/costs" + str(T), max_costs)
        np.save("sim_annealing/action" + str(T), max_actions)
        T = T * alpha
    plt.plot([i for i in range(20)], x0[:, 0])
    plt.plot([i for i in range(20)], x0[:, 1])
    plt.show()


x0 = np.array([[0., 0.] for i in range(20)])
T = 1.0
T_min = 0.00001
alpha = 0.8
simulated_annealing(x0, T, T_min, alpha)
