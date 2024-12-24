import heapq

with open('16_in.txt') as f:
    input = [list(row) for row in f.read().splitlines()]

start = tuple((i,j) for i, row in enumerate(input) for j, el in enumerate(row) if el == 'S')[0]
directions = ((-1,0), (0,1), (1,0), (0,-1)) # up, right, down, left
dir_num = 1

score = 0
path = set([start])
best_paths = set()
go_to = [(score, start, dir_num, path)]
heapq.heapify(go_to)
final_score = float('inf')
visited = dict()

while True:
    score, pos, dir_num, tmp = heapq.heappop(go_to)
    if score > final_score: break

    path = {el for el in tmp}
    # print(score, pos, dir_num, path)

    path.add(pos)
    visited.update({pos:score})

    if input[pos[0]][pos[1]] == 'E': 
        best_paths = best_paths.union(path)
        final_score = score
        continue

    score += 1
    dir_numbers = (dir_num, (dir_num + 1) % 4, (dir_num - 1) % 4)
    for k, dir_num in enumerate(dir_numbers):
        i = pos[0] + directions[dir_num][0]
        j = pos[1] + directions[dir_num][1]

        if k == 1: score += 1000

        if input[i][j] == '#' or (i,j) in visited and score > visited[(i,j)] + 1000: continue
        heapq.heappush(go_to, (score, (i, j), dir_num, path))

for i in range(len(input)):
    for j in range(len(input[0])):
        if (i,j) in best_paths: input[i][j] = 'O'

# print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in input]))
print('Part one:', final_score)
print('Part two:', len(best_paths))