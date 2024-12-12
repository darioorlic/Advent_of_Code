import numpy as np

with open('07_in.txt') as f:
    input = f.read().splitlines()

input = [el.split(' ') for el in input]

results = tuple()
numbers = tuple()
for row in input:
    results += (int(row[0][0:-1]),)
    numbers += (tuple((int(el)) for el in row[1:]),)
# print(numbers)

def calculate(numbers, operators):
    ans = numbers[0]
    for number, operator in zip(numbers[1:], operators):
        if operator == 0:
            ans += number
        elif operator == 1:
            ans *= number
        else:
            ans = int(str(ans) + str(number))
    return(ans)

ans1 = 0
for result, row in zip(results, numbers):
    bits = len(row) - 1
    for iter in range(2 ** bits):
        operators = [int(el) for el in list(np.base_repr(iter, base = 2))]
        operators = [0] * (bits - len(operators)) + operators
        if calculate(row, operators) == result:
            ans1 += result
            break

print('First answer:', ans1)

ans2 = 0
for result, row in zip(results, numbers):
    bits = len(row) - 1
    for iter in range(3 ** bits):
        operators = [int(el) for el in list(np.base_repr(iter, base = 3))]
        operators = [0] * (bits - len(operators)) + operators
        if calculate(row, operators) == result:
            ans2 += result
            break

print('Second answer:', ans2)