from collections import deque

with open("data/10.txt") as f:
    raw = list(f.read().splitlines())

matching_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
res1 = 0
for line in raw:
    stack_openers = deque()
    for char in line:
        if char in "([{<":
            stack_openers.append(char)
        else:
            last_opener = stack_openers.pop()
            if matching_pairs[last_opener] != char:
                res1 += points[char]
                break
print("#1:", res1)

points2 = {")": 1, "]": 2, "}": 3, ">": 4}
multiplier = 5
scores = []
for line in raw:
    corrupted_line = False
    stack_openers = deque()
    for char in line:
        if char in "([{<":
            stack_openers.append(char)
        else:
            last_opener = stack_openers.pop()
            if matching_pairs[last_opener] != char:
                corrupted_line = True
                break
    if corrupted_line:
        continue
    line_score = 0
    while (len(stack_openers) > 0):
        last_opener = stack_openers.pop()
        needed_closer = matching_pairs[last_opener]
        line_score = line_score * 5 + points2[needed_closer]
    if line_score > 0:
        scores.append(line_score)
sorted_scores = sorted(scores)
n_incomplete = len(sorted_scores)
res2 = sorted_scores[n_incomplete // 2]
print("#2:", res2)


def test_10():
    assert res1 == 390993
    assert res2 == 2391385187
