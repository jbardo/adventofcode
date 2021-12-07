"""
#1: 1226
#2: 1252
"""
import math


def count_increases(measurements):
    """Count number of times next integer is higher than previous one in measurements list."""
    count = 0
    prev = math.inf
    for el in measurements:
        cur = int(el)
        if cur > prev:
            count += 1
        prev = cur
    return count


with open("data/01.txt") as f:
    raw = list(map(int, f.read().splitlines()))

# 1
print("#1:", count_increases(raw))

# 2
transformed = [raw[i] + raw[i + 1] + raw[i + 2] for i in range(0, len(raw) - 2)]
print("#2:", count_increases(transformed))
