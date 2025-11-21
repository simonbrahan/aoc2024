import re

def mul_pairs(data):
    pairs_as_strings = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
    return [(int(a), int(b)) for a, b in pairs_as_strings]


with open('input.txt', 'r') as file:
    data = file.read().rstrip()

print(sum(a * b for a, b in mul_pairs(data)))
