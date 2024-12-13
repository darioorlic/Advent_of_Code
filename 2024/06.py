from time import perf_counter

t0 = perf_counter()

with open('06_in.txt', 'r') as f:
    input = tuple(tuple(el) for el in f.read().splitlines())

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
t1 = perf_counter()
print(f'Time: {t1-t0:.3}s')

# Second part #######

def get_map(obstacle, obstacles, map, update = False):
    out = dict()
    for pos_num in range(4):
        pos1 = (obstacle[0] + directions[pos_num][0], obstacle[1] + directions[pos_num][1])
        if update or pos1 not in map:

            dir_num = (pos_num - 1) % 4
            direction = directions[dir_num]
            direction_left = directions[(dir_num - 1) % 4]
            i, j = pos1
            pos2 = i + direction[0] + direction_left[0], j + direction[1] + direction_left[1]

            encountered = False
            encountered_left = False
            while True:
                ni, nj = i + direction[0], j + direction[1]
                if not (ni in range(maxI) and nj in range(maxJ)): 
                    if not encountered: out.update({pos1:'E'})
                    break
                li, lj = ni + direction_left[0], nj + direction_left[1]
                if (li, lj) in obstacles: encountered_left = True
                if (ni, nj) in obstacles:
                    if (i, j) != pos1:
                        if not encountered:
                            out.update({pos1:(i, j)})
                        if not encountered_left:
                            out.update({(li, lj): pos2})
                    encountered = True
                if encountered and encountered_left: break
                i, j = ni, nj
    return(out)

def in_loop(pos, map):
    visited = set()
    while True:
        if pos in visited: return(1)
        if map[pos] == 'E': return(0)
        visited.add(pos)
        pos = map[pos]


# Initial map
init_map = dict()
for obstacle in fixed_obstacles:
    init_map.update(get_map(obstacle, fixed_obstacles, init_map))

# Go through all new obstacles on the path
ans2 = 0
direction = directions[init_dir_num]
visited = set([init_pos])
for tmp_obstacle, starting_pos in zip(path[1:], path[:-1]):
    if tmp_obstacle in visited: continue

    visited.add(tmp_obstacle)
    all_obstacles = fixed_obstacles.copy()
    all_obstacles.add(tmp_obstacle)

    map = init_map.copy()
    map.update(get_map(tmp_obstacle, all_obstacles, map, True))

    ans2 += in_loop(starting_pos, map)

print('Second answer:', ans2)
t2 = perf_counter()
print(f'Time: {t2-t0:.3}s')