# import math
# import matplotlib.pyplot as plt

# class LCG:
#     def __init__(self, seed, a=561860773102413563, c=0, m=2**60-93):
#         self.seed = seed
#         self.a = a
#         self.c = c
#         self.m = m
#         self.state = seed

#     def next(self):
#         self.state = (self.a * self.state + self.c) % self.m
#         return self.state / self.m  # Normalize to [0, 1)

#     def next_in_range(self, a, b):
#         return a + (b - a) * self.next()

# class MonteCarlo:
#     def __init__(self, N, PRNG_object):
#         self.N = N
#         self.PRNG = PRNG_object

#     def integrate(self, f, a, b):
#         mult = (b - a) / self.N

#         generatedValues = []
#         for _ in range(self.N):
#             randomArg = self.PRNG.next_in_range(a, b)
#             randomFuncVal = f(randomArg)

#             generatedValues.append(randomFuncVal)

#         return mult * sum(generatedValues)

# def pdf(x):  # f_X
#     return (1 / 2) * (50 / x)**(26)

# def cdf(x, monteCarlo):  # F_X
#     return monteCarlo.integrate(pdf, 50, x)

# def foo(x):
#     return 1 - (50 / x)**(25)

# if __name__ == '__main__':
#     lcg = LCG(seed=42)
#     monteCarlo = MonteCarlo(100000, lcg)

#     # Define the range for plotting
#     x_values = [x for x in range(50, 201)]  # Adjust the range as needed

#     # Calculate CDF values
#     cdf_values = [cdf(x, monteCarlo) for x in x_values]

#     # Calculate foo values
#     foo_values = [foo(x) for x in x_values]

#     # Plotting
#     plt.figure(figsize=(10, 6))
#     plt.plot(x_values, cdf_values, label='CDF(x)', color='blue')
#     plt.plot(x_values, foo_values, label='foo(x)', color='red')
#     plt.xlabel('x')
#     plt.ylabel('Function Value')
#     plt.title('CDF(x) and foo(x)')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt

class LCG:
    def __init__(self, seed, a=561860773102413563, c=0, m=2**60-93):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.state = seed

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m  # Normalize to [0, 1)

    def next_in_range(self, a, b):
        return a + (b - a) * self.next()

class MonteCarlo:
    def __init__(self, N, PRNG_object):
        self.N = N
        self.PRNG = PRNG_object

    def integrate(self, f, a, b):
        mult = (b - a) / self.N

        generatedValues = []
        for _ in range(self.N):
            randomArg = self.PRNG.next_in_range(a, b)
            randomFuncVal = f(randomArg)

            generatedValues.append(randomFuncVal)

        return mult * sum(generatedValues)

class CDM:
    def __init__(self, h):
        self.h = h

    def diff(self, f, x):
        numerator = f(x + self.h) - f(x - self.h)
        denominator = 2 * self.h

        return numerator / denominator

class Newton:
    def __init__(self, f, CDM_object, tol=1e-6, max_iter=1000):
        self.f = f
        self.CDM = CDM_object
        self.tol = tol
        self.max_iter = max_iter

    def solve(self, y, x0):
        x = x0
        for _ in range(self.max_iter):
            f_x = self.f(x) - y
            f_prime_x = self.CDM.diff(self.f, x)
            if abs(f_prime_x) < 1e-10:
                raise ValueError("Derivative is zero, method fails.")
            x_new = x - f_x / f_prime_x
            if abs(x_new - x) < self.tol:
                return x_new
            x = x_new
        raise ValueError(f"Method did not converge.({x_new})")

if __name__ == '__main__':
    lcg = LCG(seed=42)
    monteCarlo = MonteCarlo(100000, lcg)

    def erf(x):
        def integrand(t):
            return np.exp(-t**2)

        integral_value = monteCarlo.integrate(integrand, 0, x)
        return (2 / np.sqrt(np.pi)) * integral_value

    # Пример использования
    x = 1.0
    erf_value = erf(x)
    print(f"erf({x}) ≈ {erf_value}")

    def cdf(x): # F_X
        return 1/2 + 1/2 * erf((np.log(x) - 2)/(np.sqrt(0.4)))

    cdm = CDM(h=1e-6)
    newton = Newton(cdf, cdm, tol=1e-6, max_iter=1000)

    def inverse(y, x0): # x = f^-1(y)
        return newton.solve(y, x0)

    data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    guesses = [0, 3, 6, 9, 12, 15]

    for el in data:
        for guess in guesses:
            try:
                print(f'inverse cdf({el}): {newton.solve(el, guess)}')
                break
            except:
                print(f'guess {guess} did not converge')
        print('-'*200)

    # Define the range for plotting
    x_values = [x for x in range(50, 201)]  # Adjust the range as needed

    # Calculate CDF values
    cdf_values = [cdf(x) for x in x_values]

    # Calculate foo values
    foo_values = [1 - (50 / x)**(25) for x in x_values]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, cdf_values, label='CDF(x)', color='blue')
    plt.plot(x_values, foo_values, label='foo(x)', color='red')
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.title('CDF(x) and foo(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
