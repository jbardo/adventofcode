#1
h = 0
v = 0
with open('day2.txt') as f:
    for line in f.readlines():
        instruction, X = line.split()
        X = int(X)
        if instruction == 'forward':
            h += X
        elif instruction == 'up':
            v -= X
        elif instruction == 'down':
            v += X
        else:
            raise RuntimeError(instruction, X)
print("#1:", h*v)

#2
h, v, aim = 0, 0, 0
with open('day2.txt') as f:
    for line in f.readlines():
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
print("#2:", h*v)