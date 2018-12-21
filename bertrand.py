import numpy as np
import math


n = 5
length = math.sqrt(3)

def estimate(X):
    count = {'long': 0, 'short': 0}
    for i in range(len(X)):
        count

def generate_1(n):
    result = []
    for i in range(n):
        x = np.random.rand(2) * 2 * math.pi
        result.append([np.array([math.cos(x[0]), math.sin(x[0])]), np.array([math.cos(x[1]), math.sin(x[1])])])
    return result

print(length)