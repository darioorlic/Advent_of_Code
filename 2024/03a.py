import re

with open('03_in.txt', 'r') as f:
    input = f.read()
# print(input)

# input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
input = re.sub('mul', '\nmul', input).splitlines()
input = [element for element in input if bool(re.search(r'mul\(\d{1,3},\d{1,3}\)', element))]
input = [[int(re.search(r'(\d{1,3}),(\d{1,3})', element)[1]), int(re.search(r'(\d{1,3}),(\d{1,3})', element)[2])] for element in input]

ans1 = sum([element[0] * element[1] for element in input])
print(ans1)