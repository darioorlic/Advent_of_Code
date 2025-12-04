with open('2025/04_in.txt') as f:
    input_ = f.read()
input_ = [[ch for ch in line] for line in input_.splitlines()]

def remove_rolls(input_: list[list[str]]) -> tuple[int, list[list[str]]]:
    from copy import deepcopy
    inp = deepcopy(input_)
    access_rolls = 0
    for i, line in enumerate(inp):
        for j, ch in enumerate(line):
            n_around = -1
            if ch != '@': continue
            up_lim, down_lim = max(0, i-1), min(i+2, len(inp))
            left_lim, right_lim = max(0, j-1), min(j+2, len(line))
            for k in range(up_lim, down_lim ):
                n_around += inp[k][left_lim : right_lim ].count('@')
                n_around += inp[k][left_lim : right_lim ].count('x')
            if n_around < 4:  
                access_rolls += 1
                inp[i][j] = 'x'
    # remove x-es
    for i, line in enumerate(inp):
        for j, ch in enumerate(line):
            if inp[i][j] == 'x': inp[i][j] = '.'

    return access_rolls, inp

print('Part 1:', remove_rolls(input_)[0])

ans2 = 0
while True:
    removed, input_ = remove_rolls(input_)
    if removed == 0: break
    ans2 += removed
    
print('Part 2:', ans2)