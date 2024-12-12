with open('02_in.txt', 'r') as f:
    input = [[int(num) for num in line.split(' ')] for line in f]
# print(input)

total = 0
for report in input:
    safe = 0
    if report[1] - report[0] == 0: continue
    sign = (report[1] - report[0]) / abs(report[1] - report[0])

    for level in range(1,len(report)):
        diff = sign * (report[level] - report[level - 1])
        if diff >= 1 and diff <= 3: safe += 1

    # print(str(sign) + ', ' + str(safe))
    if safe == len(report) - 1: total += 1

print(total)