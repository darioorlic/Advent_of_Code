from time import perf_counter
from functools import cache

t0 = perf_counter()
with open('19_in.txt') as f:
    input = f.read().splitlines()

patterns = set(input[0].split(', '))
designs = tuple(input[2:])

@cache
def match_pattern(find):
    ways = 0
    for pattern in patterns:
        if find[:len(pattern)] == pattern:
            if find[len(pattern):] in patterns:
                ways += 1
            ways += match_pattern(find[len(pattern):])
    return(ways)

possible = []
ways = []
for design in designs:
    possible.append(bool(match_pattern(design)))
    ways.append(match_pattern(design))
print('Part one:', sum(possible))
print('Part two:', sum(ways))

print(perf_counter() - t0, 's')