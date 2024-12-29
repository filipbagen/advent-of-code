from itertools import combinations


def read_antenna_positions(filename):
    antennas = {}
    with open(filename) as f:
        for r, line in enumerate(f):
            for c, val in enumerate(line.strip()):
                if val != '.':
                    if val not in antennas:
                        antennas[val] = []
                    antennas[val].append((r, c))
    return antennas


def get_line_of_sight(pos1, pos2, grid_rows, grid_cols):
    r1, c1 = pos1
    r2, c2 = pos2
    points = set()

    dr = r2 - r1
    dc = c2 - c1

    # Check both directions
    for direction in [-1, 1]:
        r, c = r1, c1
        while 0 <= r < grid_rows and 0 <= c < grid_cols:
            points.add((r, c))
            r += dr * direction
            c += dc * direction

    return points


# Read input
antennas = read_antenna_positions('input.txt')
grid_rows = grid_cols = len(open('input.txt').readline().strip())

# Calculate visible points
visible_points = set()
for positions in antennas.values():
    for pos1, pos2 in combinations(positions, 2):
        visible_points.update(get_line_of_sight(
            pos1, pos2, grid_rows, grid_cols))

print(len(visible_points))
