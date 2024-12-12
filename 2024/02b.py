with open('02_in.txt', 'r') as f:
    input = [[int(num) for num in line.split(' ')] for line in f]
# print(input)

total = 0
for report in input:

    for removed in range(len(report)):
        tmp_report = report.copy()
        del tmp_report[removed]

        if tmp_report[1] - tmp_report[0] == 0: continue
        sign = (tmp_report[1] - tmp_report[0]) / abs(tmp_report[1] - tmp_report[0])

        for level in range(1,len(tmp_report)):
            diff = sign * (tmp_report[level] - tmp_report[level - 1])
            if not(diff >= 1 and diff <= 3):
                break
        else: 
            total += 1
            break

    # print(str(sign) + ', ' + str(safe))

print(total)