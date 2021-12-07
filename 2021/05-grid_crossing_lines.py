with open("data/05.txt") as f:
    raw = f.readlines()

lines = [line.rstrip().split(" -> ")for line in raw]
for line in lines:
    for i, val in enumerate(line):
        line[i] = list(map(int, val.split(",")))


def is_vertical(line):
    return line[0][0] == line[1][0]


def is_horizontal(line):
    return line[0][1] == line[1][1]


def is_hv(line):
    return is_horizontal(line) or is_vertical(line)


def is_diag(line):
    return abs(line[1][0] - line[0][0]) == abs(line[1][1] - line[0][1])


def is_diag_right(line):
    def sign(n):
        return (n >= 0) - (n < 0)
    return sign(line[1][0] - line[0][0]) == sign(line[1][1] - line[0][1])


def is_hvd(line):
    return is_hv(line) or is_diag(line)


def find_maxes(lines, hv_only):
    xmax, ymax = 0, 0
    for line in lines:
        if (hv_only is False) or is_hv(line):
            xmax = max(xmax, line[0][0], line[1][0])
            ymax = max(ymax, line[0][1], line[1][1])
    return xmax, ymax


def add_lines_hv(grid, lines):
    for line in lines:
        if not is_hv(line):
            continue
        xlow, xhigh = min(line[0][0], line[1][0]), max(line[0][0], line[1][0])
        ylow, yhigh = min(line[0][1], line[1][1]), max(line[0][1], line[1][1])
        for i in range(xlow, xhigh + 1):
            for j in range(ylow, yhigh + 1):
                try:
                    grid[i][j] += 1
                except IndexError as e:
                    print(xlow, xhigh, ylow, yhigh)
                    print(i, j, len(grid), len(grid[0]))
                    raise e
    return grid


def add_lines_d(grid, lines):
    for line in lines:
        if not is_diag(line):
            continue
        xlow, xhigh = min(line[0][0], line[1][0]), max(line[0][0], line[1][0])
        ylow, yhigh = min(line[0][1], line[1][1]), max(line[0][1], line[1][1])
        if is_diag_right(line):
            for i in range(xhigh - xlow + 1):
                grid[xlow + i][ylow + i] += 1
        else:
            for i in range(xhigh - xlow + 1):
                grid[xlow + i][yhigh - i] += 1

    return grid


def count_higher(grid, threshold):
    res = 0
    for line in grid:
        res += sum(1 for val in line if val >= threshold)
    return res


xmax_hv, ymax_hv = find_maxes(lines, True)
grid_hv = [[0] * (ymax_hv + 1) for _ in range(xmax_hv + 1)]
grid_hv = add_lines_hv(grid_hv, lines)
res1 = count_higher(grid_hv, 2)
print("#1:", res1)

xmax_hvd, ymax_hvd = find_maxes(lines, False)
grid_hvd = [[0] * (ymax_hvd + 1) for _ in range(xmax_hvd + 1)]
grid_hvd = add_lines_hv(grid_hvd, lines)
grid_hvd = add_lines_d(grid_hvd, lines)
res2 = count_higher(grid_hvd, 2)
print("#2:", res2)


def test_05():
    assert res1 == 7297
    assert res2 == 21038
