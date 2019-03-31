def sum1(r, n):
    return sum([r**x for x in range(n)])

def sum2(r, n):

    return ((r ** n) // (r - 1)) - (1 // (r - 1))

def run():
    from time import time as t
    from random import randint as rand

    data = [(rand(2, 2500), rand(1, 1200)) for _ in range(32000)]

    start = t()
    x = [sum1(*x) for x in data]
    print(t() - start)

    start = t()
    y = [sum2(*x) for x in data]
    print(t() - start)

    print(set(x) ^ set(y))
