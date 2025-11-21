def is_safe(row):
    direction = None
    last_num = row[0]

    for num in row[1:]:
        if not direction:
            if num < last_num:
                direction = 'down'
            elif num > last_num:
                direction = 'up'
            else:
                return False
    
        difference = abs(num - last_num)

        if not 1 <= difference <= 3:
            return False

        if direction == 'up' and num < last_num:
            return False

        if direction == 'down' and num > last_num:
            return False

        last_num = num

    return True


safe_row_count = 0
with open('input.txt') as input_file:
    for line in input_file:
        if is_safe([int(i) for i in line.split()]):
            safe_row_count += 1

print(safe_row_count)
