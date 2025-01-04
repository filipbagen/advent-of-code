with open('input.txt') as f:
    top, bottom = f.read().split('\n\n')


grid = [list(line) for line in top.splitlines()]
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
    current_row, current_col = row, col
    go = True

    while True:
        current_row += direction_row
        current_col += direction_col
        char = grid[current_row][current_col]

        if char == '#':
            go = False
            break
        if char == 'O':
            targets.append((current_row, current_col))
        if char == '.':
            break

    if not go:
        continue

    grid[row][col] = '.'
    grid[row + direction_row][col + direction_col] = '@'
    for box_row, box_col in targets[1:]:
        grid[box_row + direction_row][box_col + direction_col] = 'O'

    row += direction_row
    col += direction_col

print(sum(100 * row + col for row in range(rows)
      for col in range(cols) if grid[row][col] == 'O'))
