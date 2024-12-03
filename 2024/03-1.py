import re

with open("input.txt") as f:
    lines = f.read()

result = 0

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", lines)
result = sum(int(x) * int(y) for x, y in matches)

print(result)
