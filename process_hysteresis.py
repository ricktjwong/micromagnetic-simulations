import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['figure.figsize'] = 8, 5
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'


def process_hysteresis():
    # idxs = [i for i in range(10)]
    # for i in idxs:
    #     df = pd.read_csv('./permalloy_hysteresis/permalloy_single_y.' + str(i) + '.out/table.txt', delimiter="\t")
    #     x = df['B_exty (T)']
    #     y = df['my ()']
    #     y = y/max(y)
    #     plt.plot(x, y, label=str(60 + (10*i)) +'nm')
    # plt.legend()
    # plt.savefig('halbach-current-design-antiparallel.pdf', dpi=1000)

    idxs = [i for i in range(4, 10)]
    for i in idxs:
        df = pd.read_csv('./perm_double_y/perm_double_y.' + str(i) + '.out/table.txt', delimiter="\t")
        x = df['B_exty (T)']
        y = df['my ()']
        y = y/max(y)
        plt.plot(x, y, label=str(60 + (10*i)) + 'nm')
    plt.xlim(-0.075, 0.075)
    # plt.legend()

    # widths = [i for i in range(100, 160, 10)]
    # for w in widths:
    #     df = pd.read_csv('./data/hysteresis/mumax/double/cobalt_x-600-100/y-100-100-' + str(w) + '.txt', delimiter="\t")
    #     x = df['B_exty (T)']
    #     y = df['my ()']
    #     y = y/max(y)
    #     plt.plot(x, y, label=str(w)+'nm')
    #     # plt.xlim([-0.2, 0.2])
    #     plt.legend()
    # plt.savefig('cobalt_y-100-100-x.pdf', dpi=1000)
    plt.savefig('perm_double_coercivity.pdf', dpi=1000)
    plt.show()


process_hysteresis()
