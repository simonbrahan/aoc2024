from collections import defaultdict

left_col = []
right_col_counts = defaultdict(int)
with open('input.txt') as input_file:
    for line in input_file:
        left_num, right_num = [int(num) for num in line.split()]
        left_col.append(left_num)
        right_col_counts[right_num] += 1

score = 0
for num in left_col:
   score += num * right_col_counts[num]

print(score)
