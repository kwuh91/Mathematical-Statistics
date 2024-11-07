import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


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
    
    # def next_in_range(self, a, b):
    #     return a + (b - a) * self.next()


import scipy.special
import numpy as np


if __name__ == '__main__':

    # ----------------------------------PART1----------------------------------

    def cdf(x): # F_X
        return float(1/2 + 1/2 * \
            scipy.special.erf((np.log(x) - 2)/(np.sqrt(0.4))))

    cdm    = CDM(h=1e-6)
    newton = Newton(cdf, cdm, tol=1e-6, max_iter=1000)

    def inverse(y, x0): # x = f^-1(y)
        return newton.solve(y, x0)

    n = 120
    lcg = LCG(seed=42)

    # ----------------------------------PART2----------------------------------

    data = [lcg.next() for _ in range(n)]
    # print(data)

    guesses = [0, 3, 6, 9, 12, 15, 18, 21]
    for ind, el in enumerate(data):
        for attempt, guess in enumerate(guesses):
            try: 
                inv_value = inverse(el, guess)
                data[ind] = inv_value
                break
            except:
                pass

            if attempt == len(guesses) - 1:
                raise Exception('Solution was not found')
    
    # print(sorted(data))

    # ----------------------------------PART3----------------------------------

    mini, maxi = min(data), max(data)
    # print(mini, maxi)

    range_ = maxi - mini
    # print(range_)

    # ----------------------------------PART4----------------------------------

    trunc = lambda x : int(str(x)[:str(x).index('.')])

    k = 1 + trunc(np.log2(n))
    # print(k)
    
    h = range_ / k
    # print(h)

    # ----------------------------------PART5----------------------------------
    grouped_data = []

    begin = mini
    for i in range(k):
        end = begin + h

        middle = (begin + end) / 2
        freq = sum(begin <= el < end for el in data)
        # for el in data:
        #     if begin <= el < end:
        #         print(f'{begin} <= {el} < {end}')

        relative_freq = freq / n

        print(i, begin, end, middle, freq, relative_freq)

        grouped_element = {
            'interval numero': i,
            'interval': f'[{begin}, {end})',
            'middle': middle,
            'frequency': freq,
            'relative frequency': relative_freq
        }
        grouped_data.append(grouped_element)

        begin = end        

    for element in grouped_data:
        print(element['interval numero'], 
              element['interval'], 
              element['middle'], 
              element['frequency'], 
              element['relative frequency'])
