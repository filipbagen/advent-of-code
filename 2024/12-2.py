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


def sides(region):
    edges = {}
    for (row, col) in region:
        for neighbor_row, neighbor_col in [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]:
            if (neighbor_row, neighbor_col) in region:
                continue
            edge_row = (row + neighbor_row) / 2
            edge_col = (col + neighbor_col) / 2
            edges[(edge_row, edge_col)] = (edge_row - row, edge_col - col)

        seen = set()
        side_count = 0
        for edge, direction in edges.items():
            if edge in seen:
                continue
            seen.add(edge)
            side_count += 1
            edge_row, edge_col = edge
            if edge_row % 1 == 0:  # if edge row is an integer
                for difference_row in [-1, 1]:
                    current_row = edge_row + difference_row
                    while edges.get((current_row, edge_col)) == direction:
                        seen.add((current_row, edge_col))
                        current_row += difference_row

            else:
                for difference_col in [-1, 1]:
                    current_col = edge_col + difference_col
                    while edges.get((edge_row, current_col)) == direction:
                        seen.add((edge_row, current_col))
                        current_col += difference_col

    return side_count


print(sum(len(region) * sides(region) for region in regions))
