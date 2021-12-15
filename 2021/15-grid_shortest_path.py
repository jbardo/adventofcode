import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

with open("data/15.txt") as f:
    grid = [[int(c) for c in s] for s in f.read().splitlines()]


def create_links(grid):
    N = len(grid)
    links = np.ndarray((N * N, N * N), np.int32)
    for j in range(N):
        for i in range(N):
            cur = j * N + i
            if (i < N - 1):
                links[cur][cur + 1] = grid[j][i + 1]
            if (j < N - 1):
                links[cur][cur + N] = grid[j + 1][i]
            if (i > 0):
                links[cur][cur - 1] = grid[j][i - 1]
            if (j > 0):
                links[cur][cur - N] = grid[j - 1][i]
    return links


def create_mask(grid, predecesors):
    N = len(grid)
    mask = [[0] * N for _ in range(N)]
    v = 9999
    while v > 0:
        j = v // N
        i = v % N
        mask[j][i] = 1
        v = predecesors[v]
    return mask


graph = csr_matrix(create_links(grid))
dist_matrix, predecesors = shortest_path(csgraph=graph, directed=True, indices=0, return_predecessors=True)
res1 = int(dist_matrix[-1])
print("#1:", res1)


def display(grid, mask=None):
    N = len(grid)

    class color:
        BLUE = '\033[1;34;48m'
        END = '\033[1;37;0m'

    for j in range(N):
        for i in range(N):
            if mask is None:
                print(grid[j][i], end="")
            else:
                print(color.BLUE * mask[j][i] + str(grid[j][i]) + color.END, end="")
        print()


display(grid, create_mask(grid, predecesors))
print("#1:", res1)

N = len(grid)
big_grid = np.ndarray((N * 5, N * 5), np.int32)
for m in range(5):
    for n in range(5):
        for j in range(N):
            for i in range(N):
                if m == 0 and n == 0:
                    big_grid[m * N + j][n * N + i] = grid[j][i]
                else:
                    if m > 0:
                        prev = big_grid[(m - 1) * N + j][n * N + i]
                    elif n > 0:
                        prev = big_grid[m * N + j][(n - 1) * N + i]
                    big_grid[m * N + j][n * N + i] = prev % 9 + 1

# Following takes too long ...
# graph2 = csr_matrix(create_links(big_grid))
# dist_matrix2, predecesors2 = shortest_path(csgraph=graph2, directed=True, indices=0, return_predecessors=True)
# res2 = int(dist_matrix2[-1])
# display(big_grid, create_mask(big_grid, predecesors2))
# print("#2:", res2)


def test_15():
    assert res1 == 553
