with open("2022/input.txt") as file:
    lines = file.readlines()

    instructions = [line.strip() for line in lines]
    X = 1
    cycles = 1
    cycleStop = [20, 60, 100, 140, 180, 220]
    list = []
    CTR = ["."] * 40 * 6

    for instruction in instructions:

        if "addx" in instruction:

            # Split the string and add the value
            line = instruction.strip().split(" ")
            value = int(line[1])

            # Adds two cycles
            for i in range(2):
                cycles += 1

                if cycles in cycleStop:
                    list.append(X * cycles)

            X += value

        else:
            for i in range(1):
                cycles += 1

                if cycles in cycleStop:
                    list.append(X * cycles)

    print(sum(list))
