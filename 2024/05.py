with open('05_in.txt', 'r') as f:
    input = f.read().splitlines()
# print(input)

empty = input.index('')

rules = tuple((int(el.split('|')[0]), int(el.split('|')[1])) for i, el in enumerate(input) if i in range(empty))
# print(rules)

pages = tuple(eval(el) for i, el in enumerate(input) if i in range(empty + 1, len(input) + 1))
# print(pages)

ans1 = 0
incorrect_pages = []
for page in pages:
    correct = True
    for rule in rules:
        try:
            if page.index(rule[0]) > page.index(rule[1]): correct = False
        except:
            continue
    if correct: 
        ans1 += page[int((len(page) - 1) / 2)]
    else:
        incorrect_pages += [list(page)]

ans2 = 0
for page in incorrect_pages:
    half = int((len(page) - 1) / 2)

    i = 0
    while i < len(page):
        if i < half:
            if bool(rules.count((page[half], page[i]))): 
                page[i], page[half] = page[half], page[i]
                i = 0
                continue
        elif i > half:
            if bool(rules.count((page[i], page[half]))): 
                page[i], page[half] = page[half], page[i]
                i = 0
                continue
        i += 1
    ans2 += page[half]

print('First answer: ' + str(ans1))
print('Second answer: ' + str(ans2))
