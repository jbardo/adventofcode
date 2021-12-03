"""
#1: 2036120
#2: 2015547716
"""

with open("day2.txt") as f:
    raw = list(f.readlines())

#1
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
print("#1:", h*v)  # 

#2
def compute_hv_aim(lines):
    h, v, aim = 0, 0, 0
    for line in lines:
        instruction, X = line.split()
        X = int(X)
        if instruction == 'forward':
            h += X
            v += aim*X
        elif instruction == 'up':
            aim -= X
        elif instruction == 'down':
            aim += X
        else:
            raise RuntimeError(instruction, X)
    return h, v, aim
h, v, _ = compute_hv_aim(raw)
print("#2:", h*v)