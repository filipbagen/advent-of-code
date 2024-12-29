from itertools import product
with open('input.txt') as f:
    equations = f.read().strip().splitlines()


def evaluate_expression(numbers, operations):
    result = numbers[0]
    for i, op in enumerate(operations):
        if op == '+':
            result += numbers[i + 1]
        else:
            result *= numbers[i + 1]
    return result


def solve_equation(value, numbers):
    n = len(numbers)
    # Generate all possible combinations of + and *
    for ops in product(['+', '*'], repeat=n-1):
        if evaluate_expression(numbers, ops) == value:
            return True
    return False


# Process each equation
total = 0
for equation in equations:
    value, *numbers = equation.split(': ')
    value = int(value)
    numbers = list(map(int, numbers[0].split()))

    if solve_equation(value, numbers):
        total += value

print(f"Total: {total}")
