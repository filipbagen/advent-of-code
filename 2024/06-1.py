# Read input file and solve
with open('input.txt') as f:
    input_data = f.read()


def find_guard(map_grid):
    for i in range(len(map_grid)):
        for j in range(len(map_grid[i])):
            if map_grid[i][j] in '^v<>':
                return i, j, map_grid[i][j]
    return None


def next_direction(current):
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return turns[current]


def solve_guard_patrol(map_data):
    # Convert input to 2D grid
    map_grid = [list(line.strip())
                for line in map_data.splitlines() if line.strip()]
    rows, cols = len(map_grid), len(map_grid[0])

    # Movement vectors for each direction
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    # Track visited positions
    visited = set()

    # Find initial guard position
    guard = find_guard(map_grid)
    if not guard:
        return 0

    row, col, facing = guard
    visited.add((row, col))

    while True:
        # Get movement vector for current direction
        dr, dc = directions[facing]
        next_row, next_col = row + dr, col + dc

        # Check if guard would move out of bounds
        if (next_row < 0 or next_row >= rows or
                next_col < 0 or next_col >= cols):
            break

        # Check if obstacle ahead
        if map_grid[next_row][next_col] == '#':
            # Turn right
            facing = next_direction(facing)
        else:
            # Move forward
            row, col = next_row, next_col
            visited.add((row, col))
            map_grid[row][col] = facing

    return len(visited)


result = solve_guard_patrol(input_data)
print(result)
