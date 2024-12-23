with open('23_in.txt') as f:
    input = tuple(set(el.split('-')) for el in f.read().splitlines())
# print(input)

three_set = []
t_three_set = []
pcs = input[-1]
for i, el1 in enumerate(input[:-1]):
    pcs = pcs.union(el1)
    for el2 in input[i+1:]:
        if bool(el1.intersection(el2)) and el1.difference(el2).union(el2.difference(el1)) in input:
            union = el1.union(el2)
            if union not in three_set:
                three_set.append(union)
                for pc in union:
                    if pc[0] == 't':
                        t_three_set.append(union)
                        break
        
biggest_sets = [set([pc]) for pc in pcs]
max_size = 0
updated = True
while updated:
    updated = False
    for i, set in enumerate(biggest_sets):
        for pc in pcs:
            found = True
            for found_pc in set:
                if {pc, found_pc} not in input:
                    found = False
            if found:
                biggest_sets[i] = set.union({pc})
                updated = True
                if len(biggest_sets[i]) > max_size:
                    max_size = len(biggest_sets[i])
                    biggest_set = biggest_sets[i]


# print(three_set, len(three_set))
print('Part one:', len(t_three_set))
print('Part two:', ','.join(sorted(biggest_set)))