import re

WIDTH = 101
HEIGHT = 103

robots = []
for line in open('input.txt'):
    robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

min_sf = float("inf")
best_iteration = None

for second in range(WIDTH * HEIGHT):
    # Track occupied and adjacent positions
    next_set = set()
    matching = set()

    for px, py, vx, vy in robots:
        xf, yf = (px + second * vx) % WIDTH, (py + second * vy) % HEIGHT
        if (xf, yf) in next_set:
            matching.add((xf, yf))
        # Check adjacent positions
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                next_set.add((xf + dx, yf + dy))

    # If we find enough matching positions, this is likely our answer
    if len(matching) > 256:
        best_iteration = second
        break

print(best_iteration)
