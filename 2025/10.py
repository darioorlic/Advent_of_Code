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
    from itertools import combinations_with_replacement
    i = 1
    while True:
        for pressed_buttons in combinations_with_replacement(buttons, i):
            joltage = [0] * len(final_joltage)
            for button in pressed_buttons:
                joltage = [el if j not in button else el+1 for j, el in enumerate(joltage)]            
            if joltage == final_joltage: return i
        i += 1
    
def main():
    from tqdm.contrib.concurrent import process_map
    from os import cpu_count
    input_ = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
'''
    with open('2025/10_in.txt') as f:
        input_ = f.read()
    machines = [parse_line(line) for line in input_.splitlines()]
    print('Part 1:', sum([set_lights(lights, buttons) for lights, buttons, _ in machines]))

    n_cpu = cpu_count()
    ans2 = sum(process_map(set_joltage, [joltage for _, _, joltage in machines], [buttons for _, buttons, _ in machines], max_workers=n_cpu, chunksize=n_cpu))
        
    print('Part 2:', ans2)


if __name__ == '__main__': main()