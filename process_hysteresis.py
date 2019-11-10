import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-bright')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['figure.figsize'] = 8, 5
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'

def process_mumax_double_cobalt_y():
    widths = [10 * i for i in range(10, 22, 2)]
    for w in widths:
        df = pd.read_csv('./data/mumax/double/cobalt/y-100-' + str(w) + '-100.txt', delimiter="\t")
        x = df['B_exty (T)']
        y = df['my ()']
        y = y/max(y)
        plt.plot(x, y, label=str(w)+'nm')
        plt.legend()
    # plt.savefig('y-cobalt-double-vary-gap.pdf', dpi=1000)
    plt.show()

process_mumax_double_cobalt_y()
