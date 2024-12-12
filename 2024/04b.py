import re

with open('04_in.txt', 'r') as f:
    input = f.read()
# print(input)

input = [list(el) for el in input.splitlines()]

ans2 = 0
for i in range(1, len(input) - 1):
    for j in range(1, len(input[0]) - 1):
        if input[i][j] == 'A':
            if ((input[i-1][j-1] == 'M' and input[i+1][j+1] == 'S') or (input[i-1][j-1] == 'S' and input[i+1][j+1] == 'M')) and \
            ((input[i-1][j+1] == 'M' and input[i+1][j-1] == 'S') or (input[i-1][j+1] == 'S' and input[i+1][j-1] == 'M')): ans2 += 1

# print(input)

print(ans2)