input_ = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
'''

from itertools import combinations
with open('2025/09_in.txt') as f:
    input_ = f.read()
points = []
max_x = 0
max_y = 0
for line in input_.splitlines():
    points.append(tuple(map(int, line.split(','))))
    max_x = max(points[-1][0], max_x)
    max_y = max(points[-1][1], max_y)

def calculate_area(a:tuple, b:tuple) -> int:
    return (abs(b[0] - a[0])+1) * (abs(b[1] - a[1])+1)

areas = {}
for i, j in combinations(range(len(points)), 2):
    areas[(i,j)] = calculate_area(points[i], points[j])
pairs = list(areas.keys())
pairs.sort(key = lambda x: areas[x], reverse=True)
print('Part 1:', areas[pairs[0]])

redngreen = set()
for i, j in zip(range(-1, len(points)-1), range(len(points))):
    a, b = points[i], points[j]
    if a[0] == b[0]:
        range_ = range(min(a[1], b[1]), max(a[1], b[1])+1)
        [redngreen.add((a[0], y)) for y in range_]
    else:
        range_ = range(min(a[0], b[0]), max(a[0], b[0])+1)
        [redngreen.add((x, a[1])) for x in range_]
for i in range(max_x):
    fill = False
    points_in_row = []

    for j in range(max_y):
        if (i, j) in redngreen:
            fill = not fill
            continue
        if fill: redngreen.add((i,j))
    

for pair in pairs:
    a, b = points[pair[0]], points[pair[1]]
    perimeter = set()
    range_x = range(min(a[0], b[0]), max(a[0], b[0])+1)
    range_y = range(min(a[1], b[1]), max(a[1], b[1])+1)
    [perimeter.add((x, y)) for x in [a[0], b[0]] for y in range_y]
    [perimeter.add((x, y)) for x in range_x for y in [a[1], b[1]]]
    # print(a, b)
    # print(perimeter)
    # print()

    if all([point in redngreen for point in perimeter]): break
else: raise RuntimeError('Part 2 failed.')
print(areas[pair])