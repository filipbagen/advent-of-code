with open("2022/input.txt") as file:
    [*file] = file.readline().strip()

    def distinctChar(numberOfDistinctChar):
        list = [0] * numberOfDistinctChar

        counter = 0

        for char in file:
            for i in range(numberOfDistinctChar):
                list[i] = file[counter + i]

            mySet = set(list)

            if len(mySet) != len(list):
                counter += 1
            else:
                break

        return print(counter + numberOfDistinctChar)

    # Part 1
    distinctChar(4)

    # Part 2
    distinctChar(14)
