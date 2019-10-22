import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-bright')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['figure.figsize'] = 8, 5
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'


def process_single_permalloy_y():
    widths = [10 * j for j in range(5, 11)]
    for w in widths:
        df = pd.read_csv('./data/single/permalloy/y/y-' + str(w) + 'nm.txt')
        x = df[' By']
        y = df[' my']
        plt.plot(x, y, label=str(w)+'nm')
    # plt.savefig('y-cobalt-single-sweep.pdf', dpi=1000)
    plt.legend()
    plt.show()

# process_single_cobalt_y()
# process_single_permalloy_y()
# process_double_cobalt_varygap_y()
# process_double_cobalt_varywidth_y()
