with open("data/11.txt") as f:
    grid = [[int(x) for x in line] for line in f.read().splitlines()]


def step(grid):
    flashes = 0
    for line in grid:
        for j, _ in enumerate(line):
            line[j] += 1
    for i, line in enumerate(grid):
        for j, x in enumerate(line):
            if x > 9:
                line[j] = 0
                flashes += 1 + propagate_flashes(grid, i, j)
    return flashes


def propagate_flashes(grid, i, j):
    nflashes = 0
    # neighbors4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for ii, jj in neighbors8:
        if i + ii < 0 or i + ii >= len(grid) or j + jj < 0 or j + jj >= len(grid[0]):
            continue
        if grid[i + ii][j + jj] == 0:
            continue
        grid[i + ii][j + jj] += 1
        if grid[i + ii][j + jj] > 9:
            grid[i + ii][j + jj] = 0
            nflashes += 1 + propagate_flashes(grid, i + ii, j + jj)
    return nflashes


nSteps = 100
res1 = sum(step(grid) for _ in range(nSteps))
print("#1:", res1)


def simultaneous(grid):
    for line in grid:
        if line != [0] * len(line):
            return False
    return True


res2 = nSteps
while not simultaneous(grid):
    res2 += 1
    step(grid)
print("#2:", res2)


def test_11():
    assert res1 == 1723
    assert res2 == 327
