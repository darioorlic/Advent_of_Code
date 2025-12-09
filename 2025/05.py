with open('2025/05_in.txt') as f:
    inp = f.read()
inp = inp.splitlines()

section = 0
ranges = []
ans1 = 0
for line in inp:
    if not line:
        section = 1
        continue
    if section == 0:
        start, end = line.split('-')
        ranges.append((int(start), int(end)+1))
    else:
        id = int(line)
        ans1 += any(start <= id <= end for start, end in ranges)
print('Part 1:', ans1)

ans2 = 0
ranges.sort()
lower, upper = ranges[0]
for start, end in ranges[1:]:
    if start <= upper:
        upper = max(end, upper)
    else:
        ans2 += upper - lower
        lower, upper = start, end
ans2 += upper - lower

print('Part 2:', ans2)