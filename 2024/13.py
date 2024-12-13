from re import sub

with open('13_in.txt') as f:
    input = f.read().splitlines()
# print(input)

data = [{}]
k = 0
for el in input:
    if el == '':
        data.append({})
        k += 1
        continue
    key, val = el.split(':')
    key = key.split(' ')[-1]
    val = sub('[XY=]', '', val)
    data[k].update({key:(eval(val))})

def get_coins(input, part2 = False):
    Tx, Ty = input['Prize']
    if part2: Tx, Ty = Tx + 10_000_000_000_000, Ty + 10000000000000
    Ax, Ay = input['A']
    Bx, By = input['B']

    mulB = (Ax*Ty - Ay*Tx)/(Ax*By - Ay*Bx)
    mulA = (Tx - Bx*mulB) / Ax
    if int(mulA) == mulA and int(mulB) == mulB:
        return(int(mulB) + 3 * int(mulA))
    return(0)

ans1 = 0
for el in data:
    ans1 += get_coins(el)
print('Part 1:', ans1)

ans2 = 0
for el in range(len(data)):
    ans2 += get_coins(data[el], True)
print('Part 2:', ans2)


