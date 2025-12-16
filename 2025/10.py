def parse_line(line:str) -> tuple[list[bool], list[list[int]], list[int]]:
    split = line.split()
    lights = [True if ch=='#' else False for ch in split.pop(0)[1:-1]]
    joltage = [int(ch) for ch in split.pop()[1:-1].split(',')]
    buttons = [[int(num) for num in el[1:-1].split(',')] for el in split]
    return lights, buttons, joltage

def set_lights(final_lights:list[bool], buttons:list[list[int]]) -> int:
    from itertools import combinations
    for i in range(1, len(buttons)+1):
        for pressed_buttons in combinations(buttons, i):
            lights = [False] * len(final_lights)
            for button in pressed_buttons:
                lights = [el if j not in button else not el for j, el in enumerate(lights)]            
            if lights == final_lights: return i
    else: raise RuntimeError(f'Presses not found for input {final_lights}, {buttons}.')

def set_joltage(final_joltage:list[int], buttons:list[list[int]]) -> int:
    joltage = final_joltage
    n = len(buttons)
    m = len(joltage)
    A = [[1 if i in button else 0 for button in buttons] for i in range(m)]
    import pulp as pl

    prob = pl.LpProblem("MinimizePresses", pl.LpMinimize)
    x = [pl.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(n)]

    # objective: sum of coefficients
    prob += pl.lpSum(x)
    # constraints
    for j in range(m):
        prob += pl.lpSum(A[j][i] * x[i] for i in range(n)) == joltage[j]

    pl.COIN(msg=False).solve(prob)

    return sum(int(v.value()) for v in x) #type: ignore
    
def main():
    with open('2025/10_in.txt') as f:
        input_ = f.read()
    machines = [parse_line(line) for line in input_.splitlines()]
    print('Part 1:', sum([set_lights(lights, buttons) for lights, buttons, _ in machines]))

    ans2 = sum([set_joltage(joltage, buttons) for _, buttons, joltage in machines])
        
    print('Part 2:', ans2)


if __name__ == '__main__': main()