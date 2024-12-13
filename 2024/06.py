from time import perf_counter

t0 = perf_counter()

with open('06_in.txt', 'r') as f:
    input = tuple(tuple(el) for el in f.read().splitlines())
# print(input)

maxI = len(input)
maxJ = len(input[0])

fixed_obstacles = set()
for i in range(maxI):
    for j in range(maxJ):
        if input[i][j] in ('^', '>', 'v', '<'):
            init_pos = (i, j)
        if input[i][j] == '#':
            fixed_obstacles.add((i, j))

i, j = init_pos
if input[i][j] == '^':
    init_dir_num = 0
elif input[i][j] == '>':
    init_dir_num = 1
elif input[i][j] == 'v':
    init_dir_num = 2
elif input[i][j] == '<':
    init_dir_num = 3

directions = ((-1,0), (0,1), (1,0), (0,-1)) # up, right, down, left

# First part #######

dir_num = init_dir_num
direction = directions[dir_num % 4]
path = [(i, j)]
while i in range(1, maxI - 1) and j in range(1, maxJ - 1):
    ni, nj = i + direction[0], j + direction[1]
    if input[ni][nj] == '#': 
        dir_num += 1
        direction = directions[dir_num % 4]
        continue
    i, j = ni, nj
    path.append((i, j))

print('First answer:', len(set(path)))
# path.discard(init_pos)
t1 = perf_counter()
print(f'Time: {t1-t0:.3}s')

# Second part #######

def get_map(obstacle, all_obstacles):
    out = dict()
    for pos_num in range(4):
        pos = (obstacle[0] + directions[pos_num][0], obstacle[1] + directions[pos_num][1])
        # if pos[0] in range(1, maxI - 1) and pos[1] in range(1, maxJ - 1) and pos not in all_obstacles:

        dir_num = (pos_num - 1) % 4
        direction = directions[dir_num]
        i, j = pos
        while True:
            ni, nj = i + direction[0], j + direction[1]
            if (ni, nj) in all_obstacles:
                jump = i, j
                break
            i, j = ni, nj
            if not (i in range(1, maxI - 1) and j in range(1, maxJ - 1)): 
                jump = 'E'
                break
        if jump != pos:
            out.update({pos:jump})
    return(out)

def in_loop(i, j, map):
    visited = set()
    while True:
        # print(i, j)
        if (i, j) in visited: return(1)
        if map[(i, j)] == 'E': return(0)
        visited.add((i, j))
        i, j = map[(i, j)]


# Initial map
init_map = dict()
for obstacle in fixed_obstacles:
    init_map.update(get_map(obstacle, fixed_obstacles))

# Go through all new obstacles on the path
ans2 = 0
direction = directions[init_dir_num]
visited = set([init_pos])
for tmp_obstacle, starting_pos in zip(path[1:], path[:-1]):
    if tmp_obstacle in visited: continue
    visited.add(starting_pos)
    # print(tmp_obstacle)
    all_obstacles = fixed_obstacles.copy()
    all_obstacles.add(tmp_obstacle)
    map = init_map.copy()

    # Which obstacles' maps need to be updated
    to_update = set()
    to_update.add(tmp_obstacle)
    for dir_num in range(4):
        i, j = tmp_obstacle[0] + directions[dir_num][0], tmp_obstacle[1] + directions[dir_num][1]
        while i in range(maxI) and j in range(maxJ):
            if (i, j) in all_obstacles: break
            ni, nj = i + directions[(dir_num + 1) % 4][0], j + directions[(dir_num + 1) % 4][1]
            if (ni, nj) in all_obstacles: to_update.add((ni, nj))
            i, j = i + directions[dir_num][0], j + directions[dir_num][1]
    # print(to_update)

    map = init_map.copy()
    for obstacle in to_update:
        map.update(get_map(obstacle, all_obstacles))
    # print(map)

    i, j = starting_pos
    ans2 += in_loop(i, j, map)

print('Second answer:', ans2)
t2 = perf_counter()
print(f'Time: {t2-t0:.3}s')