import re

with open('03_in.txt', 'r') as f:
    input = f.read()
# print(input)

# input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
input = re.sub(r'(mul|do)', r'\n\1', input).splitlines()
input = [element for element in input if bool(re.search(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", element))]

do = True
ans2 = 0
for element in input:
    if bool(re.search(r"do\(\)", element)):
        do = True
    elif bool(re.search(r"don't\(\)", element)):
        do = False
    elif do:
        ans2 += int(re.search(r'(\d{1,3}),(\d{1,3})', element)[1]) * int(re.search(r'(\d{1,3}),(\d{1,3})', element)[2])
              
print(ans2)