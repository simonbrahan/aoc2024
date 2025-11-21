import re

def mul_pairs(data):
    pairs_as_strings = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
    return [(int(a), int(b)) for a, b in pairs_as_strings]


with open('input.txt', 'r') as file:
    data = file.read().rstrip()

data_parts = re.split(r'(do\(\)|don\'t\(\))', data)

out = 0
doing = True
for data in data_parts:
    if data == 'do()':
        doing = True
        continue
    if data == 'don\'t()':
        doing = False
        continue

    if doing:
        out += sum(a * b for a, b in mul_pairs(data))

print(out)
