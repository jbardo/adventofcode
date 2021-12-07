with open("data/07.txt") as f:
    raw = list(map(int, f.read().rstrip("\n").split(",")))

s = sorted(raw)
median = s[len(s) // 2]
# median = s[len(s) // 2 + 1]
res1 = sum(abs(a - median) for a in s)
print("#1:", res1)

mean = sum(s) // len(s)
# mean = int(round(sum(s) / len(s)))
diff = list(abs(a - mean) for a in s)
res2 = sum((n * (n + 1) // 2) for n in diff)
print("#2:", res2)


def test_07():
    assert res1 == 325528
    assert res2 == 85015836
