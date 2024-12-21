from copy import deepcopy

with open('21_test.txt') as f:
    input = tuple(tuple(el) for el in f.read().splitlines())
# print(input)

keys = {'7':(0,0), '8':(0,1), '9':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '1':(2,0), '2':(2,1), '3':(2,2), '0':(3,1), 'A':(3,2), '^':(3,1), '<':(4,0), 'v':(4,1), '>':(4,2)} 
start = keys['A']
empty = (3,0)

def get_moves(sequences):
    paths = [[]]
    for sequence in sequences:
        sequence = [keys[el] for el in sequence]
        sequence = [start] + sequence
        # print(sequence)
        for i in range(0, len(sequence)-1):
            dy = sequence[i+1][0] - sequence[i][0]
            dx = sequence[i+1][1] - sequence[i][1]
            # print(dy, dx)

            vertical = []
            horizontal = []

            if dy > 0: vertical.extend(['v']*abs(dy))
            elif dy < 0: vertical.extend(['^']*abs(dy))

            if dx > 0: horizontal.extend(['>']*abs(dx))
            elif dx < 0: horizontal.extend(['<']*abs(dx))
            # print(vertical, horizontal)

            next_paths = []
            add1 = []
            add2 = []
            if (sequence[i][0] + dy, sequence[i][1]) != empty:
                add1 = vertical + horizontal + ['A']
            if (sequence[i][0], sequence[i][1] + dx) != empty:
                add2 = horizontal + vertical + ['A']
            for path in paths:
                if add1 != []:
                    next_paths.append(path + add1)
                if add2 != add1 and add2 != []:
                    next_paths.append(path + add2)

            # print(next_paths)
            # print()
        
            paths = deepcopy(next_paths)

    min_len = min(map(len, paths))
    out = []
    for path in paths:
        if len(path) == min_len: out.append(path)

    return(out)

for inp in input:
    out = get_moves([inp])
    for i in range(2):
        out = get_moves(out)
    print(out)
