import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-bright')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['figure.figsize'] = 8, 5
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'

def process_single_cobalt_x():
    widths = [10 * j for j in range(8, 11)]
    for w in widths:
        df = pd.read_csv('./data/single/cobalt/x/x-' + str(w) + '.txt')
        x = df[' Bx']
        y = df[' mx']
        plt.plot(x, y, label=str(w)+'nm')
    plt.legend()
    # plt.savefig('x-cobalt-single-sweep.pdf', dpi=1000)
    plt.show()


def process_single_cobalt_y():
    widths = [10 * j for j in range(5, 11)]
    for w in widths:
        df = pd.read_csv('./data/single/cobalt/y/y-' + str(w) + 'nm.txt')
        x = df[' By']
        y = df[' my']
        plt.plot(x, y, label=str(w)+'nm')
    plt.legend()
    plt.savefig('y-cobalt-single-sweep.pdf', dpi=1000)
    plt.show()


def process_double_cobalt_varygap_y():
    widths = [10 * j for j in range(4, 16, 2)]
    for w in widths:
        df = pd.read_csv('./data/double/cobalt/vary_gap/y/y-100-' + str(w) + '-150.txt')
        x = df[' By']
        y = df[' my']
        plt.plot(x, y, label=str(w)+'nm')
    plt.legend()
    plt.savefig('y-cobalt-double-vary-gap.pdf', dpi=1000)
    plt.show()


def process_double_cobalt_varywidth_y():
    widths = [10 * j for j in range(8, 20, 2)]
    for w in widths:
        df = pd.read_csv('./data/double/cobalt/vary_width/y/y-100-50-' + str(w) + '.txt')
        x = df[' By']
        y = df[' my']
        plt.plot(x, y, label=str(w)+'nm')
    plt.legend()
    plt.savefig('y-cobalt-double-vary-width.pdf', dpi=1000)
    plt.show()


def process_double_cobalt_varywidth_x():
    widths = [10 * j for j in range(10, 16, 2)]
    for w in widths:
        df = pd.read_csv('./data/double/cobalt/vary_width/x/x-100-50-' + str(w) + '.txt')
        x = df[' Bx']
        y = df[' mx']
        plt.plot(x, y, label=str(w)+'nm')
    plt.legend()
    plt.savefig('x-cobalt-double-vary-width.pdf', dpi=1000)
    plt.show()


def process_double_cobalt_varygap_x():
    widths = [10 * j for j in range(4, 12, 2)]
    for w in widths:
        df = pd.read_csv('./data/double/cobalt/vary_gap/x/x-100-' + str(w) + '-150.txt')
        x = df[' Bx']
        y = df[' mx']
        plt.plot(x, y, label=str(w)+'nm')
    plt.legend()
    plt.savefig('x-cobalt-double-vary-gap.pdf', dpi=1000)
    plt.show()


def process_double_cobalt_mumax():
    df = pd.read_csv('./data/mumax/test.txt', delimiter="\t")
    x = df['B_exty (T)']
    y = df['my ()']
    plt.plot(x, y)
    plt.legend()
    # plt.savefig('x-cobalt-double-vary-gap.pdf', dpi=1000)
    plt.show()

    df = pd.read_csv('./data/mumax/cobalt_double-100-50-100.txt', delimiter="\t")
    x = df['B_exty (T)']
    y = df['my ()']
    plt.plot(x, y)
    plt.legend()
    plt.show()

def process_single_cobalt_mumax():
    df = pd.read_csv('./data/mumax/cobalt_single-100-anis.txt', delimiter="\t")
    x = df['B_exty (T)']
    y = df['my ()']
    plt.plot(x, y)
    plt.legend()
    # plt.savefig('x-cobalt-double-vary-gap.pdf', dpi=1000)
    df = pd.read_csv('./data/mumax/cobalt_single-100.txt', delimiter="\t")
    x = df['B_exty (T)']
    y = df['my ()']
    plt.plot(x, y)
    plt.legend()
    # plt.savefig('x-cobalt-double-vary-gap.pdf', dpi=1000)
    plt.show()


# process_single_cobalt_x()
# process_single_cobalt_y()
# process_double_cobalt_varygap_y()
# process_double_cobalt_varywidth_y()
# process_double_cobalt_varywidth_x()
# process_double_cobalt_varygap_x()
# process_double_cobalt_mumax()
process_single_cobalt_mumax()
