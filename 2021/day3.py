"""
#1: 3148794
#2: 2795310
"""
from operator import eq, ne

with open("day3.txt") as f:
    raw = list(f.read().splitlines())

#1
def compute_gamma_str(elems):
    """return format: binary string"""
    N = len(elems)
    n = len(elems[0])
    gamma_sum = [0] * n
    for l in elems:
        for i, e in enumerate(l):
            gamma_sum[i] += int(e)
    gamma_list = [0] * n
    for i, e in enumerate(gamma_sum):
        if e >= N/2:  # favorizes bit 1 over 0 when equal
            gamma_list[i] = 1
    return ''.join(list(map(str,gamma_list)))

gamma_str = compute_gamma_str(raw)
n = len(gamma_str)
gamma = int(gamma_str, 2)
epsilon = int(''.join(['1'] * n), 2) ^ gamma  # get binary negation of integer without sign issue (operator '~' would give some negative number)
print("#1:", gamma * epsilon)

#2
def compute_oxy(elems: list, pos: int, ope):
    if len(elems)==1:
        return elems[0]
    g = compute_gamma_str(elems)
    oxy = []
    for el in elems:
        if ope(el[pos], g[pos]):
            oxy.append(el)
    return compute_oxy(oxy, pos+1, ope)

oxygen = int(''.join(compute_oxy(raw, 0, eq)), 2)
co2 = int(''.join(compute_oxy(raw, 0, ne)), 2)
print("#2:", oxygen * co2)