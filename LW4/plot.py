import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

k_ = 3
p_ = 0.5
n_ = 160

alpha_ = 0.01

K_Stat = 266
quantile = lambda alpha, n, p: sp.stats.binom.ppf(alpha, n, p)  # n * k

foo1 = lambda p: quantile(1 - alpha_ / 2, n_ * k_, p) - K_Stat
foo2 = lambda p: quantile(alpha_ / 2, n_ * k_, p) - K_Stat

# Plot the functions to visualize their behavior
p_values = np.linspace(0, 1, 500)
foo1_values = foo1(p_values)
foo2_values = foo2(p_values)

plt.plot(p_values, foo1_values, label='foo1')
plt.plot(p_values, foo2_values, label='foo2')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

# Use the Brent method to find the roots
try:
    underlineP = sp.optimize.brentq(foo1, 0, 1, xtol=1e-6)
    overlineP = sp.optimize.brentq(foo2, 0, 1, xtol=1e-6)
    print(f"underlineP: {underlineP}")
    print(f"overlineP: {overlineP}")
except Exception as e:
    print(f"An error occurred: {e}")
