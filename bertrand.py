import math

import numpy as np

# see qiita: https://qiita.com/kenji-kondo/items/22e7bb173fe5abbd6360

n = 1000000
EDGE = math.sqrt(3)
LONGER = 'Longer'
SHORTER = 'Shorter'
ls = {True: LONGER, False: SHORTER}


def case_1():
    seeds = np.random.rand(n, 2) * 2 * math.pi
    samples = [[
        np.array([math.cos(x[0]), math.sin(x[0])]),
        np.array([math.cos(x[1]), math.sin(x[1])])] for x in seeds
    ]
    result_count = {}
    for x in samples:
        e = ls[np.linalg.norm(x[0] - x[1]) > EDGE]
        result_count[e] = result_count[e] + 1 if e in result_count else 0
    return dict(sorted((x[0], x[1] / n) for x in result_count.items()))


def case_2():
    samples = []
    while len(samples) < n:
        seed = np.random.rand(2)
        if np.linalg.norm(seed) <= 1: samples.append(seed)
    result_count = {}
    for x in samples:
        e = ls[(2 * math.sqrt(1 - np.linalg.norm(x) ** 2)) > EDGE]
        result_count[e] = result_count[e] + 1 if e in result_count else 0
    return dict(sorted((x[0], x[1] / n) for x in result_count.items()))


def case_3():
    samples = np.random.rand(n)
    result_count = {}
    for x in samples:
        e = ls[2 * math.sqrt(1 - x ** 2) > EDGE]
        result_count[e] = result_count[e] + 1 if e in result_count else 0
    return dict(sorted((x[0], x[1] / n) for x in result_count.items()))


print('case_1: ', case_1())
print('case_2: ', case_2())
print('case_3: ', case_3())
