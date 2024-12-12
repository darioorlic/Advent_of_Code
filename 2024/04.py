import re

with open('04_in.txt', 'r') as f:
    input = f.read()
# print(input)

ans1 = len(re.findall('XMAS', input)) + len(re.findall('SAMX', input))

def xmas(text):
    text = [''.join(el) for el in text]
    text = '\n'.join(text)
    count = len(re.findall('XMAS', text)) + len(re.findall('SAMX', text))
    return(count)


list = [list(el) for el in input.splitlines()]


# Positive diagonal
text = [[list[i][j] for j in range(len(list[0]) - 1, -1, -1) for i in range(len(list)) if i + j == ij] for ij in range(len(list) + len(list[0]) - 1)]
ans1 += xmas(text)

# Vertical
text = [[list[j][i] for j in range(len(list[0]))] for i in range(len(list))]
ans1 += xmas(text)

# list = [[1,2,3], 
#         [4,5,6], 
#         [7,8,9],
#         [10,11,12]]

# Negative diagonal
text = [[list[len(list) - 1 - i][j] for j in range(len(list[0]) - 1, -1, -1) for i in range(len(list)) if i + j == ij] for ij in range(len(list) + len(list[0]) - 1)]
ans1 += xmas(text)

# print(text)

print(ans1)