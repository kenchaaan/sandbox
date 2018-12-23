import numpy as np


# calculate pi

def calculate_pi(n):
    r = {True: 0, False: 0}
    for i in range(n):
        r[np.linalg.norm(np.random.rand(2)) <= 1] += 1
        if i & 10000: print("n is: ", r[True] / i * 4)
    return r[True] / n * 4


print(calculate_pi(100000000))
