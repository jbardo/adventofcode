from collections import defaultdict
import copy

with open("data/12.txt") as f:
    raw = [s.split("-") for s in f.read().splitlines()]

connections = defaultdict(list)
for a, b in raw:
    connections[a].append(b)
    connections[b].append(a)


def is_lowercase(s):
    return s == s.lower()


def count_paths1(p, connections, visited):
    if p == "end":
        return 1
    if is_lowercase(p) and visited[p] > 0:
        return 0
    visited[p] += 1
    res = 0
    for q in connections[p]:
        res += count_paths1(q, connections, copy.deepcopy(visited))
    return res


visited1 = defaultdict(int)
res1 = count_paths1("start", connections, visited1)
print("#1:", res1)


def count_paths2(p, connections, visited):
    if p == "end":
        return 1
    if p == "start" and visited[p] > 0:
        return 0
    if is_lowercase(p) and visited[p] > 1:
        return 0
    visited[p] += 1
    res = 0
    for q in connections[p]:
        res += count_paths2(q, connections, copy.deepcopy(visited))
    return res


def count_paths2_faster(p, connections, visited):
    return


visited2 = defaultdict(int)
res2 = count_paths2("start", connections, visited2)
print("#2:", res2)


def test_12():
    assert res1 == 5178
