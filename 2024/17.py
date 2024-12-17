with open('17_in.txt') as f:
    data = f.read().splitlines()

init_registers = {'A': eval(data[0].split(' ')[-1]), 'B': int(data[1].split(' ')[-1]), 'C': int(data[2].split(' ')[-1])}
input = list(eval(data[4].split(' ')[-1]))
# print(registers, input)

def program(opcode, operand, pointer):
    global registers

    if 0 <= operand <= 3: 
        combo = operand
    elif 4 <= operand <= 6:
        combo = registers[['A', 'B', 'C'][operand - 4]]
    
    out = []
    if opcode in (0, 6, 7):
        registers[['A', 'B', 'C'][(0, 6, 7).index(opcode)]] = int(registers['A'] / 2**combo)
    elif opcode == 1:
        registers['B'] = registers['B'] ^ operand
    elif opcode == 2:
        registers['B'] = combo % 8
    elif opcode == 4:
        registers['B'] = registers['B'] ^ registers['C']
    elif opcode == 5:
        out.append(combo % 8)

    if opcode == 3 and registers['A'] != 0:
        pointer = operand
    else:
        pointer += 2

    return(out, pointer)

def run(input):
    output = []
    pointer = 0
    while pointer < len(input) - 1:
        out, pointer = program(input[pointer], input[pointer + 1], pointer)
        output.extend(out)
    return(output)

registers = init_registers.copy()
print('Part one:', ','.join(map(str, run(input))))

output = []
A_guess = 0
for i in reversed(range(len(input))):
    inp = input[i:]
    A_guess *= 8

    while True:
        registers['A'] = A_guess
        output = run(input)
        if output == inp: break
        A_guess += 1
        
print('Part two:', A_guess)
