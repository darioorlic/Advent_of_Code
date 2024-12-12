from collections import deque

with open('12_in.txt') as f:
    input = tuple(tuple(row) for row in f.read().splitlines())
# print(input)

maxI, maxJ = len(input), len(input[0])

directions = ((-1,0), (0,1), (1,0), (0,-1)) # up, right, down, left

shapes = dict()
shape_areas = dict()
visited = deque()
id = 0
tot_cost = 0
shape_outside = dict()
for i in range(maxI):
    for j in range(maxJ):
        if (i, j) in visited: continue
        letter = input[i][j]
        key = letter + str(id)
        area = 0
        circ = 0
        this_shape = set([(i, j)])
        next = deque([(i, j)])
        edges = set()

        while next != deque([]):
            ni, nj = next.pop()
            area += 1

            for pos in directions:
                pi, pj = ni + pos[0], nj + pos[1]
                if not (pi in range(maxI) and pj in range(maxJ) and input[pi][pj] == letter):
                    circ += 1
                    edges.add((pi, pj))
                elif (pi, pj) not in this_shape:
                    next.append((pi, pj))
                    this_shape.add((pi, pj))
        
        cost = area * circ
        tot_cost += cost

        shapes.update({key:this_shape})
        shape_areas.update({key:area})
        visited.extend(this_shape)
        shape_outside.update({key:edges})

        id += 1

print('First answer:', tot_cost)


# Second part ########

def get_sides(shape, inside = False):
    shape = tuple(sorted(shape))
    init_pos = (shape[0][0] - 1, shape[0][1])
    i, j = init_pos
    dir_num = 1
    sides = 0
    delete = set()

    while True:
        if not inside: delete.add((i, j))
        ahead = (i + directions[dir_num][0], j + directions[dir_num][1])
        right_dir_num = (dir_num + 1) % 4
        right = (i + directions[right_dir_num][0], j + directions[right_dir_num][1])
        if right not in shape:
            dir_num = right_dir_num
            i, j = right
            sides += 1
        else:
            if inside: delete.add(right)
            if ahead in shape:
                dir_num = (dir_num - 1) % 4
                sides += 1
            else:
                i, j = ahead
        
        if (i, j) == init_pos: break

    return(sides, delete)


shape_sides = dict()
for key, shape in shapes.items():
    sides, delete = get_sides(shape)
    shape_outside.update({key: shape_outside[key] - delete})

    while shape_outside[key] != set():
        add_sides, delete = get_sides(shape_outside[key], True)
        shape_outside.update({key: shape_outside[key] - delete})
        sides += add_sides
    
    shape_sides.update({key:sides})



tot_cost2 = 0
for key in shapes.keys():
    tot_cost2 += shape_areas[key] * shape_sides[key]

print('Second answer:', tot_cost2)
