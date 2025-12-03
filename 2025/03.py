with open('2025/03_in.txt') as f:
    inp = f.readlines()

def get_joltage(n_batteries:int) -> int:
    out = 0
    for line in inp:
        batteries = [int(ch) for ch in line.strip()]    
        index = 0
        for i in range(n_batteries-1, 0, -1):
            digit = max(batteries[index:-i])
            index = batteries.index(digit, index, -i) + 1
            out += digit * 10**i
        out += max(batteries[index:])
    return out

print('Part 1:', get_joltage(2))
print('Part 2:', get_joltage(12))