from functools import cache
with open('2025/07_in.txt') as f:
    input_ = f.read()
inp = input_.splitlines()

beam = inp[0].index('S')
beams = {beam}
ans1 = 0
for row in inp[1:]:
    to_remove = set([beam for beam in beams if row[beam] == '^'])
    ans1 += len(to_remove)
    beams.difference_update(to_remove)
    [beams.update([beam-1, beam+1]) for beam in to_remove]
print('Part 1:', ans1)

@cache
def get_timelines(beam:int, row:int) -> int:
    if row == len(inp): return 1
    if inp[row][beam] == '^': return get_timelines(beam-1, row+1) + get_timelines(beam+1, row+1)
    else: return get_timelines(beam, row+1)
print('Part 2:', get_timelines(beam, 1))
