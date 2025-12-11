from functools import cache

@cache
def find_out(node_name:str) -> int:
    if node_name == 'out': return 1
    else: return sum([find_out(next_node) for next_node in connections[node_name]])

@cache
def find_out_pt2(node_name:str, dac:bool = False, fft:bool = False) -> int:
    if node_name == 'out': 
        if dac and fft: return 1
        else: return 0
    elif node_name == 'dac': dac = True
    elif node_name == 'fft': fft = True
    return sum([find_out_pt2(next_node, dac, fft) for next_node in connections[node_name]])

def main():
    with open('2025/11_in.txt') as f:
        input_ = f.read()

    global connections 
    connections = {}
    for line in input_.splitlines():
        key, val = line.split(':')[:2]
        connections[key] = val.split()
    
    fuck_around = 'you'
    print('Part 1:', find_out(fuck_around))
    print('Part 2:', find_out_pt2('svr'))

if __name__ == '__main__': main()