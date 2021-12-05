"""
#1: 65325
#2: 4624
"""
from collections import deque
from dataclasses import dataclass

with open("day4.txt") as f:
    raw = deque(f.readlines())

numbers = list(map(int, raw.popleft().split(",")))
boards = []
while raw:
    raw.popleft()  # empty line
    board = []
    for _ in range(5):
        line = list(map(int, raw.popleft().split()))
        board.append(line)
    boards.append(board)


# 1
@dataclass
class Line:
    board_number: int
    values: list
    mask: list  # TODO: use numpy masked array instead?
    win: bool

    def is_win(self):
        self.win = all(val is True for val in self.mask)
        return self.win

    def draw_number(self, n):
        found = False
        for i, val in enumerate(self.values):
            if val == n:
                self.mask[i] = True
                found = True
        return found


@dataclass
class Board:
    board_number: int
    values: list
    mask: list
    win: bool

    def draw_number(self, n):
        found = False
        for i, line in enumerate(self.values):
            for j, val in enumerate(line):
                if val == n:
                    self.mask[i][j] = True
                    found = True
        return found

    def compute_score(self):
        return sum(self.values[i][j] for j in range(5) for i in range(5) if not self.mask[i][j])

    def display(self):
        print(f"Board #{self.board_number}:")
        for i in range(5):
            for j in range(5):
                val_str = str(self.values[i][j])
                print(' ' * (len(val_str) == 1) + val_str + ('*' if (self.mask[i][j]) else ' ') + ' ', end='')
            print('\n', end='')


allBoards = [Board(i, board, [[False] * 5 for _ in range(5)], False) for i, board in enumerate(boards)]
allLines = [Line(i, board[j], [False] * 5, False) for i, board in enumerate(boards) for j in range(5)]
allCols = [Line(i, [board[j][k] for j in range(5)], [False] * 5, False) for i, board in enumerate(boards) for k in range(5)]
allLines += allCols

winning_board = None
winning_line = None
last_n = None
last_n_index = None
win = False
for i, n in enumerate(numbers):
    last_n = n
    last_n_index = i
    for line in allLines:
        found = line.draw_number(n)
        if found:
            allBoards[line.board_number].draw_number(n)
            if line.is_win():
                win = True
                winning_line = line
                winning_board = allBoards[line.board_number]
                break
    if win:
        break

if win:
    print(f"Board {winning_board.board_number} won after {last_n_index} rounds, latest number was {last_n}")
    print(" => winning board:")
    winning_board.display()
    print(" => winning line/col:")
    print(winning_line)
    print("#1:", winning_board.compute_score() * last_n)
else:
    print("no win???")

# 2
# Reset boards / lines
print()
allBoards = [Board(i, board, [[False] * 5 for _ in range(5)], False) for i, board in enumerate(boards)]
allLines = [Line(i, board[j], [False] * 5, False) for i, board in enumerate(boards) for j in range(5)]
allCols = [Line(i, [board[j][k] for j in range(5)], [False] * 5, False) for i, board in enumerate(boards) for k in range(5)]
allLines += allCols

winning_board = None
winning_line = None
last_n = None
last_n_index = None
n_boards = len(allBoards)
n_winning_boards = 0
stop = False
for i, n in enumerate(numbers):
    last_n = n
    last_n_index = i
    for line in allLines:
        if line.win:
            continue
        found = line.draw_number(n)
        if found:
            allBoards[line.board_number].draw_number(n)
            if line.is_win():
                winning_line = line
                winning_board = allBoards[line.board_number]
                if not winning_board.win:
                    winning_board.win = True
                    n_winning_boards += 1
        if n_winning_boards >= n_boards:
            stop = True
            break
    if stop:
        break


if stop:
    print(f"Last Board {winning_board.board_number} won after {last_n_index} rounds, latest number was {last_n}")
    print(" => last winning board:")
    winning_board.display()
    print(" => last winning line/col:")
    print(winning_line)
    print("#2:", winning_board.compute_score() * last_n)
else:
    print("no win???")
