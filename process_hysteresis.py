import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['figure.figsize'] = 8, 5
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'

def process_mumax_single_cobalt_vary_z():
    """
    600 x 100 x z, vary z from 60 to 120
    """
    widths = [10 * i for i in range(6, 13, 1)]
    for w in widths:
        df = pd.read_csv('./data/mumax/single/cobalt/vary-z/y-' + str(w) + '.txt', delimiter="\t")
        x = df['B_exty (T)']
        y = df['my ()']
        y = y/max(y)
        plt.plot(x, y, label=str(w)+'nm')
        plt.legend()
    plt.savefig('y-cobalt-single-vary-z.pdf', dpi=1000)
    plt.show()

process_mumax_single_cobalt_vary_z()
