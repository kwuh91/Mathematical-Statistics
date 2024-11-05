import math
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

def pdf(x):  # f_X
    return (1 / 2) * (50 / x)**(26)

def cdf(x, monteCarlo):  # F_X
    return monteCarlo.integrate(pdf, 50, x)

def foo(x):
    return 1 - (50 / x)**(25)

if __name__ == '__main__':
    lcg = LCG(seed=42)
    monteCarlo = MonteCarlo(100000, lcg)

    # Define the range for plotting
    x_values = [x for x in range(50, 201)]  # Adjust the range as needed

    # Calculate CDF values
    cdf_values = [cdf(x, monteCarlo) for x in x_values]

    # Calculate foo values
    foo_values = [foo(x) for x in x_values]

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
