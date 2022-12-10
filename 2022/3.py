priority = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

file = open("2022/input.txt")
lines = file.readlines()

# Find common letter in every line
def partOne():
    score = 0

    for line in lines:
        line = line.strip()

        lineLength = len(line)
        middleLenght = int(lineLength / 2)

        firstHalf = line[:middleLenght]
        secondHalf = line[middleLenght:]

        commonCharacter = "".join(set(firstHalf).intersection(secondHalf))

        score += priority[commonCharacter]

    print(score)


# Find common character in every three set
def partTwo():
    score = 0

    group = []

    for line in lines:
        line = line.strip()

        group.append(line)

        if len(group) == 3:

            commonCharacter = "".join(set.intersection(*map(set, group)))

            score += int(priority[commonCharacter])

            group.clear()

    print(score)
