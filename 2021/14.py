from collections import Counter

with open("data/14.txt") as f:
    formula = f.readline().rstrip()
    f.readline()
    rules = [s.split(" -> ") for s in f.read().splitlines()]
    rules = {k: v for k, v in rules}


def step(formula, rules):
    new_formula = []
    for i in range(len(formula) - 1):
        pair = formula[i:i + 2]
        new_formula.append(formula[i])
        if pair in rules:
            new_formula.append(rules[pair])
    new_formula.append(formula[-1])
    return "".join(new_formula)


def counts_difference(formula):
    counts = Counter(formula)
    sorted_counts = counts.most_common()
    return sorted_counts[0][1] - sorted_counts[-1][1]


formula1 = formula
for n in range(10):
    formula1 = step(formula1, rules)
res1 = counts_difference(formula1)
print("#1:", res1)


# formula2 = formula1
# for n in range(30):
#     print(n, end="\r")
#     formula2 = step(formula2, rules)
# res2 = counts_difference(formula2)
# print("#2:", res2)


def test_14():
    assert res1 == 2602
