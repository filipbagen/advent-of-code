with open("2022/input.txt") as file:
    matrix = [[*char] for char in file.read().strip().split()]

    cols = len(matrix)
    rows = len(matrix[0])

    list = [0] * 4
    rim = 2 * (cols + rows) - 4
    counter = rim
    scores = []

    # Loop through every number
    for row in range(1, rows - 1):  # Skip outer rim

        for col in range(1, cols - 1):  # Spil outer rim
            currentPos = matrix[row][col]

            # Get all horizontal and vertical trees
            top = [matrix[row - i][col] for i in range(1, row + 1)]
            right = [matrix[row][col + i] for i in range(1, cols - col)]
            down = [matrix[row + i][col] for i in range(1, rows - row)]
            left = [matrix[row][col - i] for i in range(1, col + 1)]

            # print("Top: ", top, "\nRight: ", right, "\nDown: ", down, "\nLeft: ", left)

            if (
                max(top) < currentPos
                or max(right) < currentPos
                or max(down) < currentPos
                or max(left) < currentPos
            ):
                counter += 1

            score = 1
            for num in (left, right, top, down):
                tracker = 0

                for i in range(len(num)):
                    if num[i] < currentPos:
                        tracker += 1
                    elif num[i] == currentPos:
                        tracker += 1
                        break
                    else:
                        break

                score *= tracker

            scores.append(score)
            print(len(scores))

    print("\nAnswer to part 1: ", counter)
    print("\nAnswer to part 2: ", max(scores))

    # 5762400, too high
