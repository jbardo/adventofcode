"""
#1: 352151
#2: 1601616884019
"""
from time import perf_counter

with open("day6.txt") as f:
    raw = list(map(int, f.read().rstrip("\n").split(",")))

print("Init len:", len(raw))


def naive_grow(elements, nrep):
    res = elements.copy()
    for i in range(nrep):
        nnew = 0
        for i, el in enumerate(res):
            if el == 0:
                res[i] = 6
                nnew += 1
            else:
                res[i] -= 1
        res = res + [8] * nnew
    return res


def batch_grow(elements, nrep):
    counts = [0] * 9
    for item in set(elements):
        counts[item] = elements.count(item)
    for i in range(nrep):
        nnew = counts.pop(0)
        counts[6] += nnew
        counts += [nnew]
    return counts


nrep = 80
t1 = perf_counter()
res1 = len(naive_grow(raw, 80))
t2 = perf_counter()
res1bis = sum(batch_grow(raw, 80))
t3 = perf_counter()
print("#1:", res1, f"naive time elapsed: {t2 - t1:.9f} s")
print("#1:", res1bis, f"batch time elapsed: {t3 - t2:.9f} s")
nrep2 = 256
print("#2:", sum(batch_grow(raw, 256)))
