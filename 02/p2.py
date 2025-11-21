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


def variants(row):
    out = [row]
    if len(row) < 3:
        return out

    for i in range(0, len(row)):
        out.append(row[:i] + row[i+1:])

    return out


safe_row_count = 0
with open('input.txt') as input_file:
    for line in input_file:
        line_is_safe = None
        for variant in variants([int(i) for i in line.split()]):
            if is_safe(variant):
                safe_row_count += 1
                break

print(safe_row_count)
