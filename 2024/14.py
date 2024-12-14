with open('14_in.txt') as f:
    input = f.read().splitlines()

robots = dict()
for id, row in enumerate(input):
    p, v = row.split(' ')
    p = eval(p.split('=')[1])
    v = eval(v.split('=')[1])
    robots.update({id:(p, v)})
# print(robots)

maxX = 101
maxY = 103
halfX = int(maxX / 2)
halfY = int(maxY / 2)

quadrants = [0] * 4
max_time = 10**5
for time in range(1, max_time):
    for id, (p, v) in robots.items():
        p = (p[0] + v[0]) % maxX, (p[1] + v[1]) % maxY
        robots.update({id:(p, v)})
        if time == 100:
            if p[1] > halfY:
                if p[0] > halfX: quadrants[0] += 1
                if p[0] < halfX: quadrants[1] += 1
            if p[1] < halfY:
                if p[0] < halfX: quadrants[2] += 1
                if p[0] > halfX: quadrants[3] += 1
    positions = [pos[0] for pos in robots.values()]
    if len(positions) == len(set(positions)):
        ans2 = time
        break

ans1 = 1
for quadrant in quadrants:
    ans1 *= quadrant

# Draw the tree
map = [[]]
for y in range(maxY):
    for x in range(maxX):
        if bool(positions.count((x,y))):
            map[y].append('#')
        else:
            map[y].append('.')
    map.append([])
print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in map]))

print('Part one:', ans1)
print('Part two:', ans2)