with open('2025/02_in.txt') as f:
    inp = f.read()

ans1 = 0
ans2 = 0
numbers = []
for interval in inp.split(','):
    start, end = map(int, interval.split('-'))
    numbers.extend(list(range(start, end+1)))
    
for num in numbers:
    num_str = str(num)
    num_len = len(num_str)

    for i in range(num_len // 2, 0, -1):
        if num_len % i != 0: continue
        repeat = num_len // i
        test_id = num_str[:i] * repeat
        if test_id == num_str: 
            ans2 += num
            if repeat == 2: ans1 += num
            break

print('Part 1:', ans1)
print('Part 2:', ans2)