import re

max_cubes = {"red": 12, "green": 13, "blue": 14}


def parse_input():
    COLORS = ["red", "green", "blue"]

    with open('2023/input.txt', 'r') as f:
        # lines = f.readlines()
        games = [re.findall(rf"(\d+) ({'|'.join(COLORS)})", game)
                 for game in f.readlines()]

    # print(games)

    return games


def p1(puzzle_input):

    result = 0

    for game_id, sets in enumerate(puzzle_input, start=1):

        if all(max(int(num) for num, color in sets if color == c) <= max_cubes[c] for c in max_cubes):
            result += game_id

    print('Part 1', result)


def p2(puzzle_input):
    result = 0

    for sets in puzzle_input:
        min_cubes = {"red": 0, "green": 0, "blue": 0}

        for num, color in sets:
            min_cubes[color] = max(min_cubes[color], int(num))

        result += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

    print('Part 2', result)


puzzle_input = parse_input()

# Result
p1(puzzle_input)
p2(puzzle_input)
