def calculate_sqrt(n, l):
    a = [0, n / 2.0, n]
    for i in range(l):
        a = [a[0], (a[0] + a[1]) / 2, a[1]] if a[1] ** 2 >= n else [a[1], (a[1] + a[2]) / 2, a[2]]
    return a[0]


print(calculate_sqrt(5, 1000))
