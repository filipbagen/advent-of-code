def get_guard_pos(_map):
    for i in range(len(_map)):
        for j in range(len(_map[0])):
            if _map[i][j] == "^":
                return (i, j)


def patrol(_map, pos=None, idx=None):
    if not pos:
        pos = get_guard_pos(_map)
    if not idx:
        idx = 0

    # Up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows, cols = len(_map), len(_map[0])
    visited = set([pos])
    visited_entry = {}  # Track entry state for part 2

    while True:
        d = directions[idx]
        n = (pos[0] + d[0], pos[1] + d[1])

        if n[0] < 0 or n[0] >= rows or n[1] < 0 or n[1] >= cols:
            return True, visited, visited_entry

        if _map[n[0]][n[1]] == "#":
            idx = (idx + 1) % 4
            continue

        visited.add(n)
        if n not in visited_entry:
            visited_entry[n] = (pos, idx)
        elif visited_entry[n] == (pos, idx):
            return False, None, None
        pos = n


def find_loop_positions(input_data):
    _map = [list(line) for line in input_data.splitlines()]
    is_leaving, visited, visited_entry = patrol(_map)

    if visited:
        visited.remove(get_guard_pos(_map))
    loop_count = 0

    for vi, vj in visited:
        _map_copy = [row[:] for row in _map]
        _map_copy[vi][vj] = "#"
        pos = visited_entry[(vi, vj)][0]
        idx = visited_entry[(vi, vj)][1]

        if not patrol(_map_copy, pos, idx)[0]:
            loop_count += 1

    return loop_count


with open('input.txt') as f:
    print(find_loop_positions(f.read()))
