# Read and process the input
with open('input.txt') as f:
    map = f.read().strip()

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def depth_first_search(map, i, j, target, prev=-1):
    # Check bounds first
    if i < 0 or i >= len(map) or j < 0 or j >= len(map[0]):
        return set()

    visited = map[i][j]

    if visited != prev + 1:
        return set()

    if visited == target:
        return {(i, j)}

    path_count = set()

    for direction in directions:
        path_count = path_count.union(depth_first_search(
            map, i + direction[0], j + direction[1], target, visited))

    return path_count


# Convert input to 2D integer array
map = [[int(x) for x in l.strip()] for l in map.split('\n')]

s = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            paths_found = depth_first_search(map, i, j, 9)
            s += len(paths_found)
print(s)