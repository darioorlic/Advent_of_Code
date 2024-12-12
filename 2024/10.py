with open('10_in.txt') as f:
    input = tuple(tuple(int(el) for el in row) for row in f.read().splitlines())
# print(input)
maxY = len(input)
maxX = len(input[0])

zeroes = tuple((y, x) for y in range(maxY) for x in range(maxX) if input[y][x] == 0)
scores1 = [0] * len(zeroes)
scores2 = [0] * len(zeroes)
# print(zeroes)

offset = ((-1, 0), (0, 1), (1, 0), (0, -1)) # up, right, down, left

for id, zero in enumerate(zeroes):
    next_pos = [zero]
    height = 0
    
    nines = set()
    while next_pos != []:
        # print(next_pos)
        y, x = next_pos[-1]
        next_pos = next_pos[:-1]
        height = input[y][x]

        for dy, dx in offset:
            ny, nx = y + dy, x + dx
            if ny in range(maxY) and nx in range(maxX):
                if input[ny][nx] == height + 1:
                    if height + 1 == 9:
                        scores2[id] += 1
                        nines.add((ny, nx),)
                    else:
                        next_pos += [(ny, nx),]
    scores1[id] = len(nines)
    # print()

# print(scores)
print('First answer:', sum(scores1))
print('Second answer:', sum(scores2))