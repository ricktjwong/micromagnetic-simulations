import os
import random


def initialise_gridspace(x: int, y: int):
    configs = ['uniform(0, 0, 0)', 'uniform(0, 1, 0)', 'uniform(0, -1, 0)',
               'uniform(1, 0, 0)', 'uniform(-1, 0, 0)']
    with open('./boilerplate.mx3') as f:
        with open('out2.mx3', 'w') as f1:
            for line in f:
                f1.write(line)
            lines = '\n'
            lines += 'm.SetRegion(1, uniform(0, 0, 0))\n'
            lines += 'm.SetRegion(2, uniform(0, 0, 0))\n'
            lines += 'm.SetRegion(3, uniform(0, 0, 0))\n'
            lines += 'm.SetRegion(4, uniform(0, 0, 0))\n'
            lines += 'm.SetRegion(5, ' + random.choice(configs) + ')\n'
            lines += 'm.SetRegion(6, ' + random.choice(configs) + ')\n'
            lines += 'm.SetRegion(7, ' + random.choice(configs) + ')\n'
            lines += 'm.SetRegion(8, ' + random.choice(configs) + ')\n'
            lines += 'm.SetRegion(9, ' + random.choice(configs) + ')\n'
            lines += 'm.SetRegion(10, ' + random.choice(configs) + ')\n'
            lines += 'm.SetRegion(11, ' + random.choice(configs) + ')\n'
            lines += 'm.SetRegion(12, ' + random.choice(configs) + ')\n'
            lines += 'relax()\n'
            lines += 'saveas(m, "m_optimise")\n'
            lines += 'saveas(B_demag, "strayfield_optimise")\n'
            f1.write(lines)


# Initialise gridspace of (x, y) = (2, 6) with random magnetisation directions
initialise_gridspace(2, 6)
