from functools import cache

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
ans1 = str()
for el in z_values.values():
    ans1 = str(el) + ans1
ans1 = int(ans1, 2)
print('Part one:', ans1)

# Part two #####################

lefts = []
rights = []
for gate in init_gates:
    lefts.append(set(gate[:3]))
    rights.append(gate[3])
gates = [set(row) for row in init_gates]

to_swap = []

# First bit
if {'x00', 'XOR', 'y00', 'z00'} not in gates: 
    to_swap.append('z00')
    to_swap.append(rights[lefts.index({'x00', 'XOR', 'y00'})])
d = (rights[lefts.index({'x00', 'AND', 'y00'})])

# Middle bits
for i in range(1, int(len(init_values) / 2)):
    x = f'x{i:02}'
    y = f'y{i:02}'
    z = f'z{i:02}'

    # A
    a = (rights[lefts.index({x, 'XOR', y})]) 

    # Z
    if {a, 'XOR', d} in lefts:
        if rights[lefts.index({a, 'XOR', d})] != z:
            to_swap.append(z)
            to_swap.append(rights[lefts.index({a, 'XOR', d})])

    # B
    if {a, 'AND', d} in lefts:
        b = (rights[lefts.index({a, 'AND', d})])
    else:
        for left, right in zip(lefts, rights):
            if {a, 'AND'}.issubset(left):
                to_swap.append(d)
                to_swap.extend(left.difference({a, 'AND'}))
                b = (right)
                break
            if {'AND', d}.issubset(left):
                to_swap.append(a)
                to_swap.extend(left.difference({d, 'AND'}))
                b = (right)
                break
    
    # C
    c = (rights[lefts.index({x, 'AND', y})]) 

    # D
    if {b, 'OR', c} in lefts:
        d = (rights[lefts.index({b, 'OR', c})])
    else:
        for left, right in zip(lefts, rights):
            if {b, 'OR'}.issubset(left):
                to_swap.append(c)
                to_swap.extend(left.difference({b, 'OR'}))
                d = (right)
                break
            if {'OR', c}.issubset(left):
                to_swap.append(b)
                to_swap.extend(left.difference({c, 'OR'}))
                d = (right)
                break
    
# Last bit
z = f'z{int(len(init_values) / 2):02}'
if d != z:
    to_swap.extend([d, z])

print('Part two:', ','.join(sorted(set(to_swap))))