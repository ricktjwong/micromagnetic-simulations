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
    widths = [i for i in range(80, 82, 2)]
    for w in widths:
        df = pd.read_csv('./data/hysteresis/mumax/double/cobalt_x-600-70/y-70-100-' + str(w) + '.txt', delimiter="\t")
        x = df['B_exty (T)']
        y = df['my ()']
        y = y/max(y)
        plt.figure()
        plt.plot(x, y, label=str(w)+'nm')
        plt.legend()
        plt.savefig('y-cobalt-double-vary-width-' + str(w) + '-100-70.pdf', dpi=1000)
    plt.show()

process_mumax_single_cobalt_vary_z()
