from copy import deepcopy

with open('15_in.txt') as f:
    input = f.read().splitlines()

empty = input.index('')

init_map = [list(row) for row in input[:empty]]
map1 = deepcopy(init_map)
init_robot = [(i, j) for i in range(len(map1)) for j in range(len(map1[0])) if map1[i][j] == '@'][0]
moves = [el for row in input[empty + 1:] for el in row]

directions = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)} # up, right, down, left

robot = init_robot
for move in moves:
    direction = directions[move]
    pos1 = robot[0] + direction[0], robot[1] + direction[1]  

    i, j = pos1
    while True:
        if map1[i][j] == '#': break
        if map1[i][j] == '.':
            map1[i][j], map1[pos1[0]][pos1[1]] = map1[pos1[0]][pos1[1]], map1[i][j]
            map1[robot[0]][robot[1]], map1[pos1[0]][pos1[1]] = map1[pos1[0]][pos1[1]], map1[robot[0]][robot[1]] 
            robot = pos1
            break
        i, j = i + direction[0], j + direction[1]

ans1 = 0
for i, row in enumerate(map1):
    for j, el in enumerate(row):
        if el == 'O': ans1 += i*100 + j 

print('Part one:', ans1)

# Part 2 #######################

map2 = []
i, j = 0,0
boxes = dict()
id = 0
for row in init_map:
    j = 0
    map2.append([])
    for el in row:
        if el == '.':
            map2[i].extend(['.']*2)
        if el == '#':
            map2[i].extend(['#']*2)
        if el == '@':
            map2[i].extend(['@', '.'])
            robot = [i, j]
        if el == 'O':
            map2[i].extend(['[', ']'])
            boxes.update({id:[[i, j], [i, j+1]]})
            id += 1
        j += 2
    i += 1

maxI = len(map2)
maxJ = len(map2[0])

# print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in map2]))

iter = 0
for move in moves[:]:
    direction = directions[move]
    i, j = robot[0] + direction[0], robot[1] + direction[1]
    to_move = set()
    found = True

    # Horizontal
    if move in ('<','>'):
        while True:
            if map2[i][j] == '#': break
            found = False
            for key, val in boxes.items():
                if val[0] == [i,j] or val[1] == [i,j]:
                    to_move.add(key)
                    j += 2*direction[1]
                    found = True
            if not found: break
        if not found:
            robot[1] += direction[1]
            for key in to_move:
                boxes[key][0][1] += direction[1]
                boxes[key][1][1] += direction[1]

    # Vertical
    else:
        next_interval = set([j])
        while True:
            interval = next_interval.copy()
            next_interval = set()
            if sum([el == '#' for j in interval for el in map2[i][j]]) != 0: break
            found = False
            for key, val in boxes.items():
                for j in interval:
                    if val[0] == [i,j] or val[1] == [i,j]:
                        to_move.add(key)
                        next_interval.update([val[0][1], val[1][1]])
                        found = True
            if not found: break
            i += direction[0]
        if not found:
            robot[0] += direction[0]
            for key in to_move:
                boxes[key][0][0] += direction[0]
                boxes[key][1][0] += direction[0]


map3 = deepcopy(map2)
for i in range(maxI):
    for j in range(maxJ):
        if map3[i][j] not in ('#', '.'): map3[i][j] = '.'
map3[robot[0]][robot[1]] = '@'

ans2 = 0
for box in boxes.values():
    map3[box[0][0]][box[0][1]] = '['
    map3[box[1][0]][box[1][1]] = ']'
    ans2 += 100*box[0][0] + box[0][1]
print('Part two:', ans2)
# print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in map3]))