from functools import cache
def main():
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
    from time import time
    from tqdm import tqdm
    with open('2025/09_in.txt') as f:
        input_ = f.read()
    times = []
    times.append(time())
    points : list[tuple[int, int]] = []
    for line in input_.splitlines():
        x, y = line.split(',')
        points.append((int(x),int(y)))

    areas = {}
    for i, j in combinations(range(len(points)), 2):
        areas[(i,j)] = calculate_area(points[i], points[j])
    times.append(time())
    print('Areas:', times[-1] - times[-2])
    pairs = list(areas.keys())
    pairs.sort(key = lambda x: areas[x], reverse=True)
    times.append(time())
    print('Sort areas:', times[-1] - times[-2], 's')
    print('Part 1:', areas[pairs[0]])

    polygon = set()
    for i, j in zip(range(-1, len(points)-1), range(len(points))):
        a, b = points[i], points[j]
        if a[0] == b[0]:
            range_ = range(min(a[1], b[1]), max(a[1], b[1])+1)
            [polygon.add((a[0], y)) for y in range_]
        else:
            range_ = range(min(a[0], b[0]), max(a[0], b[0])+1)
            [polygon.add((x, a[1])) for x in range_]
    times.append(time())
    print('Polygon:', times[-1] - times[-2], 's')

    start = sorted(sorted(points, key = lambda x: x[1]))[0]
    global outside_polygon
    outside_polygon = get_outside_perimeter(start, polygon)
    times.append(time())
    print('Outside polygon:', times[-1] - times[-2], 's')

    for pair in tqdm(pairs):
        a, b = points[pair[0]], points[pair[1]]
        rectangle = set()
        range_x = range(min(a[0], b[0]), max(a[0], b[0])+1)
        range_y = range(min(a[1], b[1]), max(a[1], b[1])+1)
        [rectangle.add((x, y)) for x in [a[0], b[0]] for y in range_y]
        [rectangle.add((x, y)) for x in range_x for y in [a[1], b[1]]]
        # print(a, b)
        # print(rectangle)
        # print()

        for point in rectangle:
            if point_in_outside_poly(point): break
        else: break
    else: raise RuntimeError('Part 2 failed.')
    times.append(time())
    print('Find rectangle:', times[-1] - times[-2], 's')
    print('Part 2:', areas[pair])
    print('Total:', times[-1] - times[0], 's')

def calculate_area(a:tuple[int, int], b:tuple[int, int]) -> int:
    return (abs(b[0] - a[0])+1) * (abs(b[1] - a[1])+1)

def get_outside_perimeter(start:tuple[int, int], perimeter:set[tuple[int, int]]) -> set[tuple[int, int]]:
    from collections import deque
    pos = start[0]-1, start[1]
    outside_perim = {pos}
    #                   down,   right,  up,      left
    directions = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
    while True:
        i = 1
        for i, direction in enumerate(directions):
            next_pos = pos[0] + direction[0], pos[1] + direction[1]
            if next_pos in outside_perim: return outside_perim
            if next_pos not in perimeter:
                pos = next_pos
                outside_perim.add(pos)
                break
        directions.rotate(-i+1)

@cache
def point_in_outside_poly(point:tuple[int, int]) -> bool:
    return point in outside_polygon


if __name__ == '__main__': main()