with open("data/09.txt") as f:
    raw = f.read().splitlines()

grid = [list(map(int, list(line))) for line in raw]


def low_points(grid):
    low_points = []
    for i, line in enumerate(grid):
        for j, val in enumerate(line):
            if (
                (j > 0 and val >= line[j - 1]) or
                (j < (len(line) - 1) and val >= line[j + 1]) or
                (i > 0 and val >= grid[i - 1][j]) or
                (i < (len(grid) - 1) and val >= grid[i + 1][j])
            ):
                continue
            low_points.append((i, j))
    return low_points


class color:
    PURPLE = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BLACK = '\033[1;30;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'


def display_grid_low_points(grid, lpts):
    for i, line in enumerate(grid):
        for j, val in enumerate(line):
            print(color.GREEN * ((i, j) in lpts) + str(val) + color.END, end='')
        print()


lpts = low_points(grid)
res1 = sum(grid[i][j] + 1 for i, j in lpts)
display_grid_low_points(grid, lpts)
print("#1:", res1)


def expand_basin(grid, basin, i, j):
    for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if i + ii < 0 or i + ii >= len(grid) or j + jj < 0 or j + jj >= len(grid[0]):
            continue
        if (i + ii, j + jj) in basin:
            continue
        if grid[i + ii][j + jj] <= grid[i][j] or grid[i + ii][j + jj] == 9:
            continue
        basin.append((i + ii, j + jj))
        basin = expand_basin(grid, basin, i + ii, j + jj)
    return basin


def display_grid_basins(grid, lpts, basins):
    for i, line in enumerate(grid):
        for j, val in enumerate(line):
            for b in basins:
                if (i, j) in b:
                    print(color.BLUE, end='')
                    break
            print(color.GREEN * ((i, j) in lpts) + str(val) + color.END, end='')
        print()


basins = []
for pt in lpts:
    basins.append([pt])
    basins[-1] = expand_basin(grid, basins[-1], pt[0], pt[1])
display_grid_basins(grid, lpts, basins)

basins_sizes = [len(basin) for basin in basins]
basins_sizes = sorted(basins_sizes, reverse=True)
res2 = basins_sizes[0] * basins_sizes[1] * basins_sizes[2]
print("#2:", res2)


def test_09():
    assert res1 == 539
    assert res2 == 736920
