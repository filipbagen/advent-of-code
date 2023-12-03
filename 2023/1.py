import re


def parse_input():
    with open('2023/input.txt', 'r') as f:
        lines = f.readlines()
    return lines


def p1(puzzle_input):

    result = 0

    for line in puzzle_input:

        # Find all occurrences of digits (\d) in each line
        digit = ''.join(re.findall(r'\d', line))

        # Add the first and last digit to the result
        result += int(digit[0] + digit[-1])

    print(result)


def p2(puzzle_input):
    result = 0
    subs = ["on(?=e)", "tw(?=o)", "thre(?=e)", "four", "fiv(?=e)",
            "six", "seven", "eigh(?=t)", "nin(?=e)"]

    db = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
          'seven': 7, 'eight': 8, 'nine': 9,
          'on': 1, 'tw': 2, 'thre': 3, 'fiv': 5, 'eigh': 8, 'nin': 9}

    pattern = "|".join(subs) + r'|\d'

    for line in puzzle_input:
        matches = re.findall(pattern, line.strip())
        result += db[matches[0]] * 10 + db[matches[-1]]

    print(result)


puzzle_input = parse_input()

p1(puzzle_input)
p2(puzzle_input)
