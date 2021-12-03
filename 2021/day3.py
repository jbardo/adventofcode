#1
def find_gamma(elems):
    """return format: binary string"""
    N = len(elems)
    n = len(elems[0])
    gamma_sum = [0] * n
    for l in elems:
        for i, e in enumerate(l):
            gamma_sum[i] += int(e)
    gamma = [0] * n
    for i, e in enumerate(gamma_sum):
        if e >= N/2:
            gamma[i] = 1
    return ''.join(list(map(str,gamma)))

with open("day3.txt") as f:
    raw = list(f.read().splitlines())
    gamma = find_gamma(raw)

n = len(gamma)
gamma = int(gamma, 2)
epsilon = int(''.join(['1'] * n), 2) ^ gamma
print("#1:", gamma * epsilon)

#2
def compute_oxy(elems, pos):
    if len(elems)==1:
        return elems[0]
    g = find_gamma(elems)
    oxy = []
    for el in elems:
        if el[pos] == g[pos]:
            oxy.append(el)
    return compute_oxy(oxy, pos+1)

def compute_co2(elems, pos):
    if len(elems)==1:
        return elems[0]
    g = find_gamma(elems)
    co2 = []
    for el in elems:
        if el[pos] != g[pos]:
            co2.append(el)
    return compute_co2(co2, pos+1)

oxygen = int(''.join(compute_oxy(raw, 0)), 2)
co2 = int(''.join(compute_co2(raw, 0)), 2)
print("#2:", oxygen * co2)