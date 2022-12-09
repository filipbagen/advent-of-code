file = open("2022/input.txt")
lines = file.readlines()

elves = []
totalCalorie = 0

for calorie in lines:

    if calorie != "\n":
        totalCalorie += int(calorie)

    else:
        elves.append(totalCalorie)
        totalCalorie = 0

# Display most calories
print("Most calories:", max(elves))

# Sort list
elves.sort(reverse=True)
print("Top 3 elves", elves[0] + elves[1] + elves[2])
