with open('09_in.txt') as f:
    input = f.read()

# input = '2333133121414131402x'
input = tuple((int(el)) for el in list(input)[:-1])
# print(input)

id = 0
data1 = []
for i, el in enumerate(input):
    if i % 2 == 0:
        data1 += [id for _ in range(el)]
        id += 1
    else:
        data1 += ['.' for _ in range(el)]
data2 = data1.copy()

j = 0
for i in range(len(data1) - 1, -1, -1):
    if data1[i] != '.':
        while j < i:
            if data1[j] == '.':
                data1[i], data1[j] = data1[j], data1[i]
                break
            j += 1
# print(data1)

def checksum(data):
    ans = 0
    for i, el in enumerate(data):
        if el != '.':
            ans += i * el
    return(ans)
print('First answer:', checksum(data1))

# Part two ################

ids = tuple(set(data2))[:-1]

for id in reversed(ids):
    i = data2.index(id)
    num_files = data2.count(id)
    j = 0
    while j < i:
        if data2[j : j + num_files] == ['.'] * num_files:
            data2[j : j + num_files] = [id] * num_files
            data2[i : i + num_files] = ['.'] * num_files
            break
        j += 1
# print(data2)

print('Second answer:', checksum(data2))