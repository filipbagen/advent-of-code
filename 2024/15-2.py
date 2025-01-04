with open('input.txt') as f:
    top, bottom = f.read().split('\n\n')

expansion = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}

grid = [list("".join(expansion[char] for char in line))
        for line in top.splitlines()]
moves = bottom.replace('\n', "")

rows = len(grid)
cols = len(grid[0])

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == '@':
            break
    else:
        continue
    break

for move in moves:
    direction_row = {'^': -1, 'v': 1}.get(move, 0)
    direction_col = {'<': -1, '>': 1}.get(move, 0)

    targets = [(row, col)]
    go = True

    for current_row, current_col in targets:
        next_row = current_row + direction_row
        next_col = current_col + direction_col

        if (next_row, next_col) in targets:
            continue

        char = grid[next_row][next_col]

        if char == '#':
            go = False
            break
        if char == '[':
            targets.append((next_row, next_col))
            targets.append((next_row, next_col + 1))
        if char == ']':
            targets.append((next_row, next_col))
            targets.append((next_row, next_col - 1))

    if not go:
        continue

    copy = [list(row) for row in grid]

    grid[row][col] = '.'
    grid[row + direction_row][col + direction_col] = '@'

    for box_row, box_col in targets[1:]:
        grid[box_row][box_col] = '.'

    for box_row, box_col in targets[1:]:
        grid[box_row + direction_row][box_col +
                                      direction_col] = copy[box_row][box_col]

    row += direction_row
    col += direction_col

print(sum(100 * row + col for row in range(rows)
      for col in range(cols) if grid[row][col] == '['))
