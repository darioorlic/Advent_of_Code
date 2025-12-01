from math import floor
with open('2025/01_in.txt') as f:
    inp = f.readlines()

moves = []
for line in inp:
    if line[0] == 'L': moves.append(- int(line[1:]))
    else: moves.append(int(line[1:]))

pos = 50
out1 = 0
out2 = 0
for move in moves:
    on_zero = False
    next_num = pos + move
    next_pos = (next_num) % 100

    passes = floor(next_num / 100)
    out2 += abs(passes)
    if passes <= -1:
        if pos == 0 and next_pos != 0: out2 -= 1
        if pos != 0 and next_pos == 0: out2 += 1 
    if pos != 0 and next_pos == 0 and passes == 0: out2 +=1

    pos = next_pos
    if pos == 0: out1 += 1

print('Part 1:', out1)
print('Part 2:', out2)