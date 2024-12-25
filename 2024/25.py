locks = set()
keys = set()

with open('25_in.txt') as f:
    first_row = True
    height = [-1] * 5
    for row in f.read().splitlines():
        if first_row:
            if row == '#####': lock = True
            else: lock = False
            first_row = False
        for i, el in enumerate(row):
            if el == '#': height[i] += 1
        if row == '':
            if lock: locks.add(tuple(height))
            else: keys.add(tuple(height))
            first_row = True
            height = [-1] * 5
    if lock: locks.add(tuple(height))
    else: keys.add(tuple(height))

ans1 = 0 
for lock in locks:
    for key in keys:
        for a, b in zip(lock, key):
            if a + b > 5: break
        else: ans1 += 1

print('Part one:', ans1)