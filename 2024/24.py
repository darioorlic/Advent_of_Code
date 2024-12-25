with open('24_test.txt') as f:
    input = f.read().splitlines()

i = 0
init_values = dict()
while True:
    if input[i] == '': break
    init_values.update({input[i].split(': ')[0]: int(input[i].split(': ')[1])})
    i += 1

i += 1
calculations = []
while i < len(input):
    calculations.append(tuple(el for el in input[i].split(' ') if el != '->'))
    i += 1
# print(values, calculations)

def calculate(row):
    global values

    in1, operator, in2, out = row
    if operator == 'AND': val = values[in1] & values[in2]
    elif operator == 'OR': val = values[in1] | values[in2]
    elif operator == 'XOR': val = values[in1] ^ values[in2]

    values.update({out:val})

values = init_values.copy()
while calculations:
    for i, row in enumerate(calculations):
        if row[0] in values and row[2] in values:
            calculate(row)
            del calculations[i]

z_values = dict((key,val) for key, val in sorted(values.items()) if key[0] == 'z')
# print(z_values)

ans1 = str()
for el in z_values.values():
    ans1 = str(el) + ans1
ans1 = int(ans1, 2)
print('Part one:', ans1)

# Part two #####################

x_values = dict((key,val) for key, val in sorted(values.items()) if key[0] == 'x')
y_values = dict((key,val) for key, val in sorted(values.items()) if key[0] == 'y')
x_val = str()
y_val = str()
for val1, val2 in zip(x_values.values(), y_values.values()):
    x_val = str(val1) + x_val
    y_val = str(val2) + y_val
x_val = int(x_val, 2)
y_val = int(y_val, 2)
target = x_val + y_val
target = f'{target:0{len(z_values)}b}'
# print(target)

z_tagets = dict(('z' + f'{i:02}', int(val)) for i, val in enumerate(reversed(target)))
# print(z_tagets)

def get_score():
    score = 0
    for key, val in z_tagets.items():
        if val == values[key]: score += 1
        else: print(key)
    return(score)



print(get_score())