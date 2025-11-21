left_col = []
right_col = []
with open('input.txt') as input_file:
    for line in input_file:
        left_num, right_num = [int(num) for num in line.split()]
        left_col.append(left_num)
        right_col.append(right_num)

left_col.sort()
right_col.sort()

total_distance = 0
for left, right in zip(left_col, right_col):
    total_distance += abs(left - right)

print(total_distance)
