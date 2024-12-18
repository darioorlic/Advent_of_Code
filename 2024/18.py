from heapq import heapify, heappop, heappush

with open('18_in.txt') as f:
    input = tuple(eval(el) for el in f.read().splitlines())

max = 70
in_bytes = 1024

def find_path(obstacles):
    visited = dict()
    total_steps = float('inf')
    go_to = [(0, (0,0))]
    heapify(go_to)

    while bool(go_to):
        steps, pos = heappop(go_to)

        if pos == (max, max):
            total_steps = steps
            break

        steps += 1
        for direction in ((-1,0), (0,1), (1,0), (0,-1)):
            npos = pos[0] + direction[0], pos[1] + direction[1]
            
            if npos in obstacles or npos[0] not in range(max+1) or npos[1] not in range(max+1)or npos in visited and steps >= visited[npos]: continue
            visited.update({npos:steps})
            heappush(go_to, (steps, npos))

    return(total_steps)

print('Part one:', find_path(input[:in_bytes]))

# Part two ###########

for i in range(in_bytes+1, len(input)):
    inp = input[:i]
    if find_path(inp) == float('inf'):
        print('Part two:', ','.join(map(str, input[i-1])))
        break