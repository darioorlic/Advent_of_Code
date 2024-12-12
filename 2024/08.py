# Part one ############

with open('08_in.txt') as f:
    input = tuple(tuple(el) for el in f.read().splitlines())
# print(input)

antennas = set(el for row in input for el in row if el != '.')
# print(antennas)

positions  = {antenna:() for antenna in antennas}
for antenna in antennas:
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == antenna:
                positions[antenna] += ((i, j),)
# print(positions)

output = [['.' for j in i] for i in input]

for antenna in positions:
    # print()
    for m in range(len(positions[antenna])):
        for n in range(m + 1, len(positions[antenna])):
            diff = (positions[antenna][m][0] - positions[antenna][n][0], positions[antenna][m][1] - positions[antenna][n][1])
            # print(diff)

            node1 = (positions[antenna][m][0] + diff[0], positions[antenna][m][1] + diff[1])
            node2 = (positions[antenna][n][0] - diff[0], positions[antenna][n][1] - diff[1])

            if 0 <= node1[0] < len(input) and 0 <= node1[1] < len(input[0]): output[node1[0]][node1[1]] = '#'
            if 0 <= node2[0] < len(input) and 0 <= node2[1] < len(input[0]): output[node2[0]][node2[1]] = '#'

# for el in output: print(el)

ans1 = sum(el.count('#') for el in output)
print('First answer:', ans1)

# Part two ############

output2 = [['.' for j in i] for i in input]

error = 0.001
for antenna in positions:
    for m in range(len(positions[antenna])):
        for n in range(m + 1, len(positions[antenna])):
            diff = (positions[antenna][m][0] - positions[antenna][n][0], positions[antenna][m][1] - positions[antenna][n][1])
            if diff[1] == 0:
                slope = 1
                dx = 0
            else:
                slope = diff[0] / diff[1]
                dx = 1

            y, x = positions[antenna][m][0], positions[antenna][m][1]
            sign = 1
            while 0 <= round(y) < len(input) and 0 <= x < len(input[0]):
                if y - error <= round(y) <= y + error: output2[int(round(y))][x] = '#'
                x += sign * dx
                y += sign * slope
                if not (0 <= round(y) < len(input) and 0 <= x < len(input[0])) and sign == 1:
                    sign = -1
                    y, x = positions[antenna][m][0], positions[antenna][m][1]

# print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in output2]))
ans2 = sum(el.count('#') for el in output2)
print('Second answer:', ans2)