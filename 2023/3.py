import re
import string


def parse_input():
    with open('2023/input.txt', 'r') as f:
        lines = f.readlines()
    return lines


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]
SYMBOLS = set(string.punctuation) - set(".")


def check_symbol_adjacment(row, col):
    return 0 <= row < rows and 0 <= col < cols and lines[row][col] in SYMBOLS


with open("2023/input.txt") as f:
    lines = f.read().splitlines()

rows = len(lines)
cols = len(lines[0])

res = 0

for i, line in enumerate(lines):
    indexes = re.finditer(r"\d+", line)
    # print('indexes', indexes)

    for idx in indexes:
        # print('idx', idx)
        first_index = idx.start()
        last_index = idx.end() - 1

        found = []
        for dr, dc in DIRECTIONS:
            new_row = i + dr
            found.append(check_symbol_adjacment(new_row, first_index + dc))
            found.append(check_symbol_adjacment(new_row, last_index + dc))

        if any(found):
            print('idx.group()', idx.group())
            res += int(idx.group())

print(res)


# too low
# 94612

symbols = set(string.punctuation) - set(".")
adjacent_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)]


def p1(puzzle_input):
    total = 0

    for row_index, row in enumerate(puzzle_input, start=1):
        for col_index, col in enumerate(row, start=1):

            # if there is a symbol
            if col in symbols:

                # Iterate over each adjacent cell
                for row_offset, col_offset in adjacent_offsets:
                    adj_row, adj_col = row_index + row_offset, col_index + col_offset

                    # Check if the adjacent cell is within bounds and numeric
                    if 0 <= adj_row < len(puzzle_input) and 0 <= adj_col < len(puzzle_input[0]) and puzzle_input[adj_row][adj_col].isnumeric():
                        # Check full number

                        total += int(puzzle_input[adj_row][adj_col])

                # Now 'total' contains the sum of all numeric adjacent cells

    print(total)


puzzle_input = parse_input()
