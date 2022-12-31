import numpy as np

with open("2022/input.txt") as file:

    lines = file.readlines()
    movements = [
        (entry.strip().split(" ")[0], int(entry.strip().split(" ")[1]))
        for entry in lines
    ]

    head = np.array([0, 0])
    tail = np.array([0, 0])

    def updateTail(head, tail):
        differance = head - tail

        changeForTail = {
            (2, 0): (1, 0),
            (2, 1): (1, 1),
            (1, 2): (1, 1),
            (0, 2): (0, 1),
            (-1, 2): (-1, 1),
            (-2, 1): (-1, 1),
            (-2, 0): (-1, 0),
            (-2, -1): (-1, -1),
            (-1, -2): (-1, -1),
            (0, -2): (0, -1),
            (1, -2): (1, -1),
            (2, -1): (1, -1),
            # Part 2
            (2, 2): (1, 1),
            (-2, -2): (-1, -1),
            (-2, 2): (-1, 1),
            (2, -2): (1, -1),
        }

        newTailPos = tail + np.array(changeForTail.get(tuple(differance), (0, 0)))
        return newTailPos

    def updateHead(head, direction):

        if direction == "R":
            head[1] += 1
        elif direction == "L":
            head[1] -= 1
        elif direction == "U":
            head[0] += 1
        elif direction == "D":
            head[0] -= 1

        return head

    tailPos = set([tuple(tail)])

    for direction, distance in movements:

        while distance:
            head = updateHead(head, direction)
            distance -= 1
            tail = updateTail(head, tail)
            tailPos.add(tuple(tail))

    print("Part 1: ", len(tailPos))  # 6190

    # Part 2
    # Create emply list which hold every tail pos
    ropeLen = 10
    rope = [np.array([0, 0])] * ropeLen

    tailPosLast = set([tuple(rope[-1])])

    # # Iterate thourgh every tail and update its head and tail

    for direction, distance in movements:

        while distance:
            rope[0] = updateHead(rope[0], direction)
            distance -= 1

            for i in range(1, len(rope)):
                rope[i] = updateTail(rope[i - 1], rope[i])

            tailPosLast.add(tuple(rope[-1]))

    print("Part 2: ", len(tailPosLast))
    print(tailPosLast)

    # Keep track of the last tails total positions, len(set(tuple(tail[-1])))

    # 61504, too high
