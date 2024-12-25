with open('20_in.txt') as f:
    input = [list(row) for row in f.read().splitlines()]

pos = tuple((i,j) for i, row in enumerate(input) for j, el in enumerate(row) if el == 'S')[0]
directions = ((-1,0), (0,1), (1,0), (0,-1)) # up, right, down, left
maxI = len(input)
maxJ = len(input[0])

score = 0
path = []
while True:
    path.append(pos)

    if input[pos[0]][pos[1]] == 'E': 
        final_score = score
        break

    score += 1
    for direction in directions:
        i = pos[0] + direction[0]
        j = pos[1] + direction[1]

        if input[i][j] in ('.', 'E') and (i,j) not in path:
            pos = (i, j)
            break

def get_shortcuts(max_length):
    shortcut_num = 0
    for m, pos1 in enumerate(path):
        for n, pos2 in zip(range(m+1, len(path)), path[m+1:]):
            length = abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])
            if length > max_length: continue
            if n - m - length >= min_save: shortcut_num += 1
    return(shortcut_num)

min_save = 100
print('Part one:', get_shortcuts(2))
print('Part two:', get_shortcuts(20))