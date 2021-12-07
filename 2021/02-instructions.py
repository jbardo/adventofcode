with open("data/02.txt") as f:
    raw = list(f.readlines())


# 1
def compute_hv(lines):
    h, v = 0, 0
    for line in lines:
        instruction, X = line.split()
        X = int(X)
        if instruction == 'forward':
            h += X
        elif instruction == 'up':
            v -= X
        elif instruction == 'down':
            v += X
        else:
            raise RuntimeError(line, instruction, X)
    return h, v


h, v = compute_hv(raw)
res1 = h * v
print("#1:", res1)


# 2
def compute_hv_aim(lines):
    h, v, aim = 0, 0, 0
    for line in lines:
        instruction, X = line.split()
        X = int(X)
        if instruction == 'forward':
            h += X
            v += aim * X
        elif instruction == 'up':
            aim -= X
        elif instruction == 'down':
            aim += X
        else:
            raise RuntimeError(instruction, X)
    return h, v, aim


h, v, _ = compute_hv_aim(raw)
res2 = h * v
print("#2:", res2)


def test_02():
    assert res1 == 2036120
    assert res2 == 2015547716
