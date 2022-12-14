with open("2022/input.txt") as file:
    stackStrings, instructions = (
        i.splitlines() for i in file.read().strip("\n").split("\n\n")
    )

    # strip("\n"):      removes \n
    # split("\n\n"):    seperates in two arrays

    stacks = {int(digit): [] for digit in stackStrings[-1].replace(" ", "")}
    indexes = [index for index, char in enumerate(stackStrings[-1]) if char != " "]

    def displayStacks():
        print("\n\nStacks:\n")
        for stack in stacks:
            print(stack, stacks[stack])
        print("\n")

    def loadStacks():
        for string in stackStrings[:-1]:
            stackNum = 1
            for index in indexes:
                if string[index] != " ":
                    stacks[stackNum].insert(0, string[index])
                stackNum += 1

    def emptyStacks():
        for stack in stacks:
            stacks[stack].clear()

    loadStacks()

    # Part 1
    for instruction in instructions:
        instruction = (
            instruction.replace("move", "")
            .replace("from ", "")
            .replace("to ", "")
            .strip()
            .split(" ")
        )

        crates, start, destination = [int(i) for i in instruction]

        for crate in range(crates):
            removedCrate = stacks[start].pop()
            stacks[destination].append(removedCrate)

    def getStackEnds():
        answer = ""

        for stack in stacks:
            answer += stacks[stack][-1]

        return answer

    print("Answer for part 1: ", getStackEnds())

    emptyStacks()
    loadStacks()

    # Part 2
    for instruction in instructions:
        instruction = (
            instruction.replace("move", "")
            .replace("from ", "")
            .replace("to ", "")
            .strip()
            .split(" ")
        )

        crates, start, destination = [int(i) for i in instruction]

        cratesToRemove = stacks[start][-crates:]  # finding out which crates to remove
        stacks[start] = stacks[start][:-crates:]  # removing crates

        for crate in cratesToRemove:
            stacks[destination].append(crate)  # adding crates to a diff stack

    print("Answer for part 2: ", getStackEnds())
