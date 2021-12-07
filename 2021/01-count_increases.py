with open("data/01.txt") as f:
    raw = list(map(int, f.read().splitlines()))


def count_increases(arr):
    """Count number of times next integer is higher than previous one in measurements list."""
    return sum((arr[i + 1] > arr[i]) for i in range(len(arr) - 1))


res1 = count_increases(raw)
print("#1:", res1)

transformed = [raw[i] + raw[i + 1] + raw[i + 2] for i in range(0, len(raw) - 2)]
res2 = count_increases(transformed)
print("#2:", res2)


def test_01():
    assert res1 == 1226
    assert res2 == 1252
