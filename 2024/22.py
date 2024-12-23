from collections import deque

with open('22_in.txt') as f:
    input = tuple(int(el) for el in f.read().splitlines())

def generate_next(number, iterations):
    global scores, max_score
    global best_change
    current_scores = dict()
    i = 0
    changes = tuple()
    
    while True:
        previous_bananas = int(str(number)[-1])
        next_number = number * 64
        number = (next_number ^ number) % 16777216

        next_number = int(number / 32)
        number = (next_number ^ number) % 16777216

        next_number = number * 2048
        number = (next_number ^ number) % 16777216

        i += 1
        if i == iterations: break

        bananas = int(str(number)[-1])
        changes = changes + tuple([bananas - previous_bananas])
        if i > 4:
            changes = changes[1:]
            if changes not in current_scores:
                current_scores.update({changes:bananas})
        # print(number, bananas, bananas - previous_bananas)

    for change, score in current_scores.items():
        new_score = score
        if change in scores:
            new_score += scores[change]
        scores.update({change:new_score})
        if new_score > max_score:
            max_score = new_score
            best_change = change

    return(number)

max_score = 0
scores = dict()
ans1 = 0
for inp in input:
    ans1 += generate_next(inp, 2000)
print('First answer:', ans1)
print('Second answer:', max_score)
print(best_change)
