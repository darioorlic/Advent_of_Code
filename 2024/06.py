from time import perf_counter
from copy import deepcopy

t0 = perf_counter()

with open('06_in.txt', 'r') as f:
    input = f.read().splitlines()
input = [list(el) for el in input]
# print(input)

i, j = [[i, j] for i, row in enumerate(input) for j, el in enumerate(row) if el in ('^', '>', 'v', '<')][0]
init_pos = [i, j]

if input[i][j] == '^':
    init_dir_num = 0
elif input[i][j] == '>':
    init_dir_num = 1
elif input[i][j] == 'v':
    init_dir_num = 2
elif input[i][j] == '<':
    init_dir_num = 3

directions = ((-1,0), (0,1), (1,0), (0,-1)) # up, right, down, left
direction = directions[init_dir_num % 4]

obstacles = tuple()
dir_num = init_dir_num
data = deepcopy(input)
while 1 <= i < len(data) - 1 and 1 <= j < len(data[0]) - 1:
    data[i][j] = 'X'
    if data[i + direction[0]][j + direction[1]] == '#':
        dir_num += 1
        direction = directions[dir_num % 4]
        if data[i + direction[0]][j + direction[1]] == '#':
            dir_num += 1
            direction = directions[dir_num % 4]
    else:
        data[i][j] = 'X'
        i += direction[0]
        j += direction[1]
        if not bool(obstacles.count((i,j))): obstacles += ((i, j),)

ans1 = sum(el.count('X') for el in data) + 1
print('First answer:', ans1)
obstacles = obstacles[1:]
# print(obstacles)

fixed_obstacles = tuple((i, j) for i, row in enumerate(input) for j, el in enumerate(row) if el == '#')
# print(fixed_obstacles)

max_hit = 5
max_iteration = 10**10
ans2 = 0

for obstacle in obstacles:
    iteration = 0
    data = deepcopy(input)
    dir_num = init_dir_num
    direction = directions[dir_num % 4]
    if data[obstacle[0]][obstacle[1]] not in ('^', '>', 'v', '<'):
        data[obstacle[0]][obstacle[1]] = '#'
    # hit = 0
    hits = [0] * (len(fixed_obstacles) + 1)

    # print()
    # for el in data:
    #     print(el)

    i, j = init_pos
    while 1 <= i < len(data) - 1 and 1 <= j < len(data[0]) - 1 and max(hits) < max_hit and iteration < max_iteration:
        if data[i + direction[0]][j + direction[1]] == '#':
            if (i + direction[0], j + direction[1]) == obstacle:
                hits[-1] += 1
            if bool(fixed_obstacles.count((i + direction[0], j + direction[1]))):
                hits[fixed_obstacles.index((i + direction[0], j + direction[1]))] += 1
            dir_num += 1
            direction = directions[dir_num % 4]
            if data[i + direction[0]][j + direction[1]] == '#':
                if (i + direction[0], j + direction[1]) == obstacle:
                    hits[-1] += 1
                if bool(fixed_obstacles.count((i + direction[0], j + direction[1]))):
                    hits[fixed_obstacles.index((i + direction[0], j + direction[1]))] += 1
                dir_num += 1
                direction = directions[dir_num % 4]
        else:
            i += direction[0]
            j += direction[1]
        iteration += 1
    
    # print(hits)
    if max(hits) == max_hit or iteration == max_iteration: ans2 += 1

print('Second answer:', ans2)

t1 = perf_counter()
print(f'Time: {t1-t0:.2}s')