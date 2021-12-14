with open("data/13.txt") as f:
    raw = list(f.read().splitlines())

dots = set()
folds = []
for i, line in enumerate(raw):
    if "," in line:
        dots.add(tuple(map(int, line.split(","))))
    elif "=" in line:
        axis, val = line.split("=")
        axis = axis[-1]
        folds.append((axis, int(val)))


def folding(dots, fold):
    axis, val = fold
    newdots = set()
    for dot in dots:
        x, y = dot
        if axis == "x":
            if x == val:
                continue
            elif x > val:
                x = val - (x - val)
        if axis == "y":
            if y == val:
                continue
            elif y > val:
                y = val - (y - val)
        newdots.add((x, y))
    return newdots


res1 = len(folding(dots, folds[0]))
print("#1:", res1)


def display(dots):
    xmax, ymax = 0, 0
    for dot in dots:
        xmax = max(xmax, dot[0])
        ymax = max(ymax, dot[1])
    grid = [[' '] * (xmax + 1) for _ in range(ymax + 1)]
    for dot in dots:
        grid[dot[1]][dot[0]] = "#"
    for line in grid:
        print("".join(line))


newdots = dots
for fold in folds:
    prevdots = newdots
    newdots = folding(prevdots, fold)
display(newdots)
res2 = "AHPRPAUZ"


def test_13():
    assert res1 == 720
    assert res2 == "AHPRPAUZ"
