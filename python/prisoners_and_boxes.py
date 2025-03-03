import numpy as np
from math import log

def unroll(n):
    i = n
    for _ in range(50):
        i = boxes[i]
        if i == n: return True
    return False

trials, wins = 10000, 0
for _ in range(trials):
    boxes = np.arange(100)
    np.random.shuffle(boxes)
    win = all(unroll(n) for n in range(100))
    if win:
        wins += 1

print(wins / trials)
print((1 - log(2)))
