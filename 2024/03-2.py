import re

with open("input.txt") as f:
    lines = f.read()

result = 0
enabled = True
matches = re.findall(r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)', lines)


for match in matches:

    if match == "don't()":
        enabled = False
        continue

    elif match == "do()":
        enabled = True

    if enabled and match.startswith("mul("):
        result += [int(x) * int(y)
                   for x, y in [re.findall(r'\d{1,3}', match)]][0]


print(result)
