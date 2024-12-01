with open("input.txt") as f:
    lines = f.read().splitlines()

left, right = [], []
total_distance = 0

for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

for x, y in zip(sorted(left), sorted(right)):
    total_distance += abs(x - y)

print(total_distance)
