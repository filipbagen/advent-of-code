from collections import deque

with open('input.txt') as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)
cols = len(grid[0])

regions = []
seen = set()

for row in range(rows):
    for col in range(cols):
        if (row, col) in seen:
            continue
        seen.add((row, col))
        region = set({(row, col)})
        queue = deque([(row, col)])
        crop = grid[row][col]

        while queue:
            current_row, current_col = queue.popleft()
            for neighbor_row, neighbor_col in [
                (current_row - 1, current_col),
                (current_row + 1, current_col),
                (current_row, current_col - 1),
                (current_row, current_col + 1)
            ]:
                if neighbor_row < 0 or neighbor_row >= rows or neighbor_col < 0 or neighbor_col >= cols:
                    continue
                if grid[neighbor_row][neighbor_col] != crop:
                    continue
                if (neighbor_row, neighbor_col) in region:
                    continue
                region.add((neighbor_row, neighbor_col))
                queue.append((neighbor_row, neighbor_col))

        seen |= region
        regions.append(region)


def perimeter(region):
    output = 0
    for (row, col) in region:
        output += 4
        for neighbor_row, neighbor_col in [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]:
            if (neighbor_row, neighbor_col) in region:
                output -= 1

    return output


print(sum(len(region) * perimeter(region) for region in regions))
