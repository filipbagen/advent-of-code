def partOne():
    file = open("2022/input.txt")
    lines = file.readlines()

    score = 0

    dictionary = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }

    for line in lines:
        line = line.strip()
        score += dictionary[line]

    return score


def partTwo():
    file = open("2022/input.txt")
    lines = file.readlines()

    score = 0

    dictionary = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }

    for line in lines:
        line = line.strip()
        score += dictionary[line]

    return score


print(partOne())
print(partTwo())
