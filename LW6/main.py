import numpy as np
from IPython.display import Math, display
import matplotlib.pyplot as plt

# data_ = np.array([
#     [-10.038, -5.731, -3.571, -4.769, -2.148, -5.876, -2.890, -5.026, -6.664, -6.096],
#     [0.547, -6.359, -8.738, -3.841, -3.484, -5.938, -4.247, -7.160, -2.433, -3.900],
#     [-1.690, -0.590, -3.802, -4.190, -1.819, -2.458, 1.452, -3.434, -5.249, -2.010],
#     [-4.633, -3.080, -8.746, -5.190, -3.556, -2.031, -4.076, -2.690, -4.211, -2.686],
#     [-3.498, -2.744, -3.635, -6.060, -4.377, -3.914, -2.641, -5.916, -4.041, -2.953],
#     [-6.094, -6.146, -2.992, -4.370, -0.334, -6.045, -2.156, -5.746, -2.191, -6.026],
#     [-2.762, -5.168, -3.052, -2.823, -6.320, -2.055, -3.915, -4.372, -0.723, -3.751],
#     [-4.142, -1.953, -4.221, 0.238, -2.718, -5.712, -2.016, -3.995, -7.838, -3.634],
#     [-3.843, -1.986, -3.188, -1.993, -6.454, -4.969, -5.130, -6.158, -2.055, -3.492],
#     [-5.332, -9.888, -2.272, -5.609, -3.733, -6.413, -2.637, -3.782, -4.319, -2.973],
#     [-4.319, -3.607, -3.343, -3.979, -2.975, -5.756, -5.843, -4.214, -6.592, -6.628],
#     [-1.026, -1.497, -5.495, -4.451, -3.347, -4.243, -3.505, -1.886, -3.364, -3.669]
# ])

data_ = np.array([
    [-3.442, 1.295, 3.672, 2.354, 5.238, 1.136, 4.421, 2.071, 0.269, 0.894],
    [8.202, 0.605, -2.011, 3.375, 3.767, 1.068, 2.928, -0.276, 4.924, 3.31],
    [5.741, 6.951, 3.417, 2.991, 5.599, 4.896, 9.197, 3.823, 1.827, 5.389],
    [2.504, 4.212, -2.021, 1.891, 3.689, 5.366, 3.117, 4.641, 2.968, 4.645],
    [3.752, 4.582, 3.601, 0.934, 2.785, 3.294, 4.695, 1.092, 3.155, 4.352],
    [0.896, 0.839, 4.309, 2.793, 7.233, 0.95, 5.228, 1.28, 5.19, 0.972],
    [4.562, 1.915, 4.243, 4.495, 0.648, 5.34, 3.294, 2.791, 6.805, 3.474],
    [3.044, 5.452, 2.957, 7.862, 4.61, 1.317, 5.383, 3.205, -1.022, 3.602],
    [3.373, 5.415, 4.093, 5.407, 0.501, 2.135, 1.957, 0.826, 5.34, 3.759],
    [1.735, -3.277, 5.101, 1.43, 3.494, 0.545, 4.699, 3.44, 2.85, 4.33]
])

data_ = data_.T
new_data_ = []

for i in range(len(data_)):
    for j in range(len(data_[i])):
        new_data_.append(data_[i][j])

data_ = new_data_
data_

# alpha = 0.05
# a0 = -3.5
# sigma0 = 2
# a1 = -4
# sigma1 = 2
# epsilon = 0.1
# n = 120
# beta = 0.137
# overlineX = -4.01523
# S2 = 3.91551
# C1 = -3.8

alpha = 0.1
a0 = 3
sigma0 = 2.1
a1 = 3.5
sigma1 = 2.2
epsilon = 0.1
n = 100
# beta = 0.99981
beta = 0.137
overlineX = 3.17705
S2 = 5.1431775
C1 = 2.7180587

def decorate_plot(ax, x_ticks, xname, yname, loc=(-0.025, -0.3)):
    SIZE_TICKS = 10

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # axis names
    ax.set_xlabel(xname, fontsize=15)
    ax.xaxis.set_label_coords(0.98, 0.05)

    ax.set_ylabel(yname, rotation=0, fontsize=15)
    ax.yaxis.set_label_coords(0.025, 0.95)

    ax.set_xticks(x_ticks)

    # Adjust the font size of the tick labels
    ax.tick_params(axis='both', which='major', labelsize=SIZE_TICKS)

    plt.legend(fontsize=10, loc=loc)

    # Update font settings
    plt.rcParams.update({'font.family': 'serif', 'font.size': 12})

    # Adjust layout
    plt.tight_layout()

for beta in np.arange(0.01, 0.9 + 0.05 + 0.01 + 0.05, 0.05):

    A_ = (1 - beta)/alpha
    B_ = beta/(1 - alpha)

    print(f'A: {A_}')
    print(f'B: {B_}')

    def Z(j):
        res = 1
        for i in range(0, j + 1):
            res *= np.exp((a0**2 - a1**2)/(2*sigma1**2) + (a1 - a0)/sigma1**2 * data_[i])
        return res

    def buildBar(filename):
        RED = '#6F1D1B'

        _, ax = plt.subplots(figsize=(10, 6))

        x_values = np.arange(0, n)
        y_values = [Z(int(x)) for x in x_values]

        ax.plot(x_values, 
            y_values, 
            color=RED, 
            linestyle='-', 
            linewidth=1.5,
            label='Z(j)')
        
        ax.axhline(y=A_, color='green', linestyle='--', label=f'A')
        ax.axhline(y=B_, color='blue', linestyle='--', label=f'B')

        decorate_plot(ax, np.arange(0,n + 10,10), 'j', '', loc='best')

        # plt.savefig(f'{filename}.png', dpi=300, transparent=True)

        plt.show()

    buildBar('iterative_crit_A_B')