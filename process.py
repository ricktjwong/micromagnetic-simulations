import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-bright')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['figure.figsize'] = 8, 5
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default'] = 'regular'

# widths = [10 * j for j in range(5, 11)]

# for w in widths:
#     df = pd.read_csv('./data/single/cobalt/y/y-' + str(w) + 'nm.csv')
#     x = df[' By']
#     y = df[' my']
#     plt.plot(x, y)

# plt.savefig('y-cobalt-single-sweep.pdf', dpi=1000)
# plt.show()

widths = [10 * j for j in range(10, 11)]

for w in widths:
    df = pd.read_csv('./data/single/cobalt/x/x-' + str(w) + 'nm.csv')
    x = df[' Bx']
    y = df[' mx']
    plt.plot(x, y)

plt.savefig('x-cobalt-single-sweep.pdf', dpi=1000)
plt.show()

# widths = [10 * j for j in range(10, 14, 2)]

# for w in widths:
#     df = pd.read_csv('./data/double/cobalt/vary_width/y/y-100-' + str(w) + '.csv')
#     x = df[' By']
#     y = df[' my']
#     plt.plot(x, y)

# plt.savefig('y-cobalt-double-sweep-width.pdf', dpi=1000)
# plt.show()

# widths = [10 * j for j in range(10, 22, 2)]

# for w in widths:
#     df = pd.read_csv('./data/double/cobalt/vary_width/x/x-100-' + str(w) + '.csv')
#     x = df[' Bx']
#     y = df[' mx']
#     plt.plot(x, y)

# plt.savefig('x-cobalt-double-sweep-width.pdf', dpi=1000)
# plt.show()

# widths = [10 * j for j in range(5, 16, 1)]

# for w in widths:
#     df = pd.read_csv('./data/double/cobalt/vary_gap/y/y-100-' + str(w) + '-150.csv')
#     x = df[' By']
#     y = df[' my']
#     plt.figure()
#     plt.plot(x, y)
# plt.show()

# plt.savefig('x-cobalt-double-sweep-width.pdf', dpi=1000)
# plt.show()
