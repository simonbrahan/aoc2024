def count_xmasses(grid):
    out = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if is_cross(grid, x, y):
                out += 1

    return out


def is_cross(grid, x, y):
    if grid[x][y] != 'A':
        return False

    back_stroke = get_back_stroke(grid, x, y)
    if back_stroke not in ['MAS', 'SAM']:
        return False

    forward_stroke = get_forward_stroke(grid, x, y)
    if forward_stroke not in ['SAM', 'MAS']:
        return False

    return True


def get_back_stroke(grid, x, y):
    if x == 0 or y == 0:
        return None

    try:
        return grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1]
    except IndexError:
        return None


def get_forward_stroke(grid, x, y):
    if x == 0 or y == 0:
        return None

    try:
        return grid[x-1][y+1] + grid[x][y] + grid[x+1][y-1]
    except IndexError:
        return None


input = []
with open('input.txt') as f:
    for line in f:
        input.append(list(line.strip()))

print(count_xmasses(input))
