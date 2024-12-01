with open("input.txt") as f:
    lines = f.read().splitlines()

left, right = [], []
similarity_score = 0

for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

for num in left:
    similarity_score += right.count(num) * num

print(similarity_score)
