def count_xmasses(grid):
    out = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            out += count_xmasses_from_pos(grid, x, y)

    return out


def count_xmasses_from_pos(grid, x, y):
    directions = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]

    out = 0
    for direction in directions:
        if find_word(grid, x, y, direction, 'XMAS'):
            out += 1

    return out


def find_word(grid, x, y, direction, word):
    if word == '':
        return True

    if x < 0 or y < 0:
        return False

    try:
        current_letter = grid[y][x]
    except IndexError:
        return False

    if current_letter == word[0]:
        return find_word(grid, x+direction[0], y+direction[1], direction, word[1:])

    return False


input = []
with open('input.txt') as f:
    for line in f:
        input.append(list(line.strip()))

print(count_xmasses(input))
