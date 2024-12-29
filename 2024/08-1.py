from collections import defaultdict
from itertools import combinations

with open('input.txt') as f:
    lines = list(map(str.strip, f.readlines()))

antenna = defaultdict(set)
num_rows = len(lines)
num_cols = len(lines[0])

for r, line in enumerate(lines):
    for c, val in enumerate(line):
        if val != '.':
            antenna[val].add((r, c))

antinodes = set()
for freq in antenna:
    for (r1, c1), (r2, c2) in combinations(antenna[freq], 2):
        dr = r2 - r1
        dc = c2 - c1
        antinodes.add((2 * r1 - r2, 2 * c1 - c2))
        antinodes.add((2 * r2 - r1, 2 * c2 - c1))

result = len([1 for r, c in antinodes if 0 <=
              r < num_rows and 0 <= c < num_cols])
print(result)
