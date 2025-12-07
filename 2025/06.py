from math import prod
with open('2025/06_in.txt') as f:
    input_ = f.read()

def calculate(input_:str, right_left: bool) -> int:
    inp = input_.splitlines()
    operators = inp.pop().split()
    if not right_left:
        numbers = [list(map(int, line.split())) for line in inp]
        numbers = list(map(list, zip(*numbers)))
    else:
        inp = zip(*[[ch for ch in row] for row in inp])
        numbers = [[]]
        for el in inp:
            num = ''.join(el)
            if num.strip() == '': numbers.append([])
            else: numbers[-1].append(int(num))
    return sum([sum(row) if operator == '+' else prod(row) for operator, row in zip(operators, numbers)])

print('Part 1:', calculate(input_, False))
print('Part 2:', calculate(input_, True))
