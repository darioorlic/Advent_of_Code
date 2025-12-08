def main():
    import numpy as np
    from math import prod
    
    # Convert junctions in input to dict(index: coords)
    with open('2025/08_in.txt') as f:
        input_ = f.read()
    n_connections = 1000
    inp = input_.splitlines()
    junctions = {}
    for i, line in enumerate(inp):
        junctions[i] = np.array(list(map(int, line.split(',')))) 

    # Get distance between each pair and sort the pairs by distance
    distances = {}
    for i in range(len(junctions)-1):
        for j in range(i+1, len(junctions)):
            distances[(i, j)] = np.linalg.norm(junctions[j] - junctions[i])
    pairs = list(distances.keys())
    pairs.sort(key = lambda x: distances[x])

    # Get the sizes of the 3 biggest groups after n_connections
    groups = [{junction} for junction in junctions]
    for _ in range(n_connections):
        a, b = pairs.pop(0)
        groups = make_connection(a, b, groups)
    groups.sort(key = lambda x: len(x), reverse=True)
    print('Part 1:', prod([len(group) for group in groups[:3]]))

    # Get the junctions in the last connection that constructs a complete network
    a, b = 0, 0
    while len(groups) > 1:
        a, b = pairs.pop(0)
        groups = make_connection(a, b, groups)
    print('Part 2:', junctions[a][0] * junctions[b][0])

def make_connection(a:int, b:int, groups:list[set]) -> list[set]:
    modify_groups = []
    for i, group in enumerate(groups):
        if a in group or b in group: modify_groups.append(i) 
    if len(modify_groups) == 2: 
        groups[modify_groups[0]].update(groups[modify_groups[1]])
        del(groups[modify_groups[1]])
    return groups

if __name__ == '__main__':
    main()