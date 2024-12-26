from functools import cache
from copy import deepcopy

with open('24_in.txt') as f:
    input = f.read().splitlines()

i = 0
init_values = dict()
while True:
    if input[i] == '': break
    init_values.update({input[i].split(': ')[0]: int(input[i].split(': ')[1])})
    i += 1

i += 1
init_gates = []
while i < len(input):
    init_gates.append([el for el in input[i].split(' ') if el != '->'])
    i += 1
# print(values, gates)

@cache
def solve_gate(in1, operator, in2, out):
    if operator == 'AND': val = in1 & in2
    elif operator == 'OR': val = in1 | in2
    elif operator == 'XOR': val = in1 ^ in2
    return({out:val})

def calculate_values(gates):
    values = init_values.copy()
    done = set()
    while len(done) < len(gates):
        for i, gate in enumerate(gates):
            if i not in done and gate[0] in values and gate[2] in values:
                values.update(solve_gate(values[gate[0]], gate[1], values[gate[2]], gate[3]))
                done.add(i)
    return(values)


values = calculate_values(init_gates)

z_values = dict((key,val) for key, val in sorted(values.items()) if key[0] == 'z')
print(z_values)
ans1 = str()
for el in z_values.values():
    ans1 = str(el) + ans1
ans1 = int(ans1, 2)
# print('Part one:', ans1)

# Part two #####################

# Get the desired value of z from x and y
x_values = dict((key,val) for key, val in sorted(values.items()) if key[0] == 'x')
y_values = dict((key,val) for key, val in sorted(values.items()) if key[0] == 'y')
x_val = str()
y_val = str()
target = str()
for val1, val2 in zip(x_values.values(), y_values.values()):
    x_val = str(val1) + x_val
    y_val = str(val2) + y_val
    target = str(val1 & val2) + target
x_val = int(x_val, 2)
y_val = int(y_val, 2)
# target = x_val + y_val
# target = f'{target:0{len(z_values)}b}'
# print(target)
z_tagets = dict(('z' + f'{i:02}', int(val)) for i, val in enumerate(reversed(target)))
print(z_tagets)

# Compare the obtained value of z with the target value of z
def get_score(values):
    score = 0
    for key, val in z_tagets.items():
        if val == values[key]: score += 1
        # else: print(key)
    return(score)
print(get_score(values))

def swap_outputs(init_gates, score, init_swapped = set(), depth = 0):
    if depth == 2: return
    for i in range(len(init_gates)):
        if i in init_swapped: continue
        for j in range(i+1, len(init_gates)):
            if j in init_swapped: continue
            swapped = init_swapped.copy()
            gates = deepcopy(init_gates)
            gates[i][3], gates[j][3] = gates[j][3], gates[i][3]
            swapped = swapped.union({i,j})

            new_score = get_score(calculate_values(gates))
            if new_score == len(z_tagets): return(swapped)
            if new_score > score+1:
                out = swap_outputs(gates, new_score, swapped, depth + 1)
    return(out)
            
print(swap_outputs(init_gates, get_score(values)))