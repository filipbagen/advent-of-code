with open("2022/input.txt", "r") as tasks:

    partOne = 0
    partTwo = 0

    for taskPair in tasks:
        first, second = taskPair.strip().split(",")

        l1, l2 = [int(num) for num in first.split("-")]
        r1, r2 = [int(num) for num in second.split("-")]

        s1 = set(range(l1, l2 + 1))
        s2 = set(range(r1, r2 + 1))

        if s1.issubset(s2) or s2.issubset(s1):
            partOne += 1

        if s1.intersection(s2):
            partTwo += 1

print(partOne)
print(partTwo)
