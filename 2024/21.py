from functools import cache
from itertools import repeat

with open('21_in.txt') as f:
    input = tuple(tuple(el) for el in f.read().splitlines())
# print(input)

keys = {'7':(0,0), '8':(0,1), '9':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '1':(2,0), '2':(2,1), '3':(2,2), '0':(3,1), 'A':(3,2), '^':(3,1), '<':(4,0), 'v':(4,1), '>':(4,2)} 
start = keys['A']
empty = (3,0)

@cache
def get_length(sequence, depth = 0):
    sequence = tuple(keys[el] for el in sequence)
    sequence = (start,) + sequence
    depth += 1
    length = 0
    for i in range(1, len(sequence)):
        dy = sequence[i][0] - sequence[i-1][0]
        dx = sequence[i][1] - sequence[i-1][1]

        vertical = tuple()
        horizontal = tuple()

        if dy > 0: vertical = ('v',) * abs(dy)
        elif dy < 0: vertical = ('^',) * abs(dy)

        if dx > 0: horizontal = ('>',)*abs(dx)
        elif dx < 0: horizontal = ('<',)*abs(dx)

        add1 = tuple()
        add2 = tuple()
        if (sequence[i-1][0] + dy, sequence[i-1][1]) != empty:
            add1 = vertical + horizontal + ('A',)
        if (sequence[i-1][0], sequence[i-1][1] + dx) != empty:
            add2 = horizontal + vertical + ('A',)
        
        to_add = {el for el in set([add1, add2]) if el != ()}
        if depth == 26: length += min(map(len, to_add))
        else: length += min(map(get_length, to_add, repeat(depth)))
            
    return(length)

ans1 = 0
ans2 = 0
for inp in input:
    number = int(''.join(inp[:-1]))
    ans1 += get_length(inp, 23) * number
    ans2 += get_length(inp) * number
print('Part one:', ans1)
print('Part two:', ans2)