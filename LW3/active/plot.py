# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import lognorm

# # Parameters
# mu = 2
# sigma = np.sqrt(0.2)

# # Create the log-normal distribution
# lognorm_dist = lognorm(s=sigma, scale=np.exp(mu))

# # Define the foo function
# # def foo(x):
# #     return lognorm_dist.cdf(x)

# def foo(x):
#     return lognorm_dist.pdf(x)

# # Define the inv_foo function
# def inv_foo(y):
#     return lognorm_dist.ppf(y)

# # Generate y values
# # y_values = np.linspace(0.01, 0.99, 100)  # Avoid extreme values 0 and 1 for numerical stability
# x_values = np.linspace(0, 20, 100)

# # Compute corresponding x values using inv_foo
# # x_values = inv_foo(y_values)
# y_values = foo(x_values)

# print(y_values)

# # Plot the inv_foo function
# # plt.plot(y_values, x_values, label='inv_foo(y)')
# plt.plot(x_values, y_values, color='#6F1D1B')
# plt.xlabel('x')
# plt.ylabel('$F_X(x) = \\frac{1}{2} + \\frac{1}{2} \\text{erf} \\left( \\frac{\\ln(x) - 2}{\\sqrt{0.4}} \\right)$')

# plt.ylim(-2.5, 3)

# ax = plt.gca()
# ax.set_aspect('equal', adjustable='box')

# plt.legend()
# plt.grid(True)

# plt.rcParams.update({'font.family': 'serif', 'font.size': 12})
# plt.savefig('cdf.png', dpi=300, transparent=True)


# plt.show()

# #3c0061

import numpy as np
import matplotlib.pyplot as plt

# Define the PDF function
def pdf(x):
    return 1 / (np.sqrt(0.4 * np.pi) * x) * np.exp(-(np.log(x) - 2)**2 / 0.4)

# Generate a range of x-values
x_values = np.linspace(0.01, 20, 1000)  # Avoid x=0 to prevent division by zero

# Compute the corresponding y-values using the PDF function
y_values = pdf(x_values)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='PDF')
plt.xlabel('x')
plt.ylabel('PDF(x)')
plt.title('Probability Density Function')
plt.legend()
plt.grid(True)
plt.show()
