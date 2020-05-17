# 주사위를 여러번 시행할 경우 특정 사건
import numpy as np
from itertools import product

# sampling
def dice(N):
    a = np.arange(1, 7)
    b = product(a, repeat=N)
    c = [x for x in b]
    return c

# extract event
def event(iterable, ev):
    d = []
    for x in iterable:
        if np.sum(x) == ev:
            d.append(x)
    return d

prob = len(event(dice(2), 7)) / len(dice(2))

print(dice(2))
print(event(dice(2), 7))
print(prob)