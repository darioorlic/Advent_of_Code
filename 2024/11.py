from functools import cache

with open('11_in.txt') as f:
    input = f.read()

# input = '125 17'

data = [int(el) for el in input.split(' ')]
# print(data)

@cache
def calc_len(iter, number):
    if iter == 0: return(1)
    iter -= 1
    split = list(str(number))
    if number == 0:
        return(calc_len(iter, 1))
    elif len(split) % 2 == 0:
        a = int(''.join(split[:int(len(split) / 2)]))
        b = int(''.join(split[int(len(split) / 2):]))
        return(calc_len(iter, a) + calc_len(iter, b))
    else:
        return(calc_len(iter, number * 2024))

ans1 = sum(calc_len(25, num) for num in data)
print('First answer:', ans1)
ans2 = sum(calc_len(75, num) for num in data)
print('Second answer:', ans2)
# print(calc_len.cache_info())