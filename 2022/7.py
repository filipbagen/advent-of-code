with open("2022/input.txt") as file:
    commands = [command.strip() for command in file.readlines()]

# keep track of path
path = "/home"
dirs = {"/home": 0}

# Process every command
for command in commands:

    # Commands that starts with $
    if command[0] == "$":

        # Do nothing when listning directories or files
        if command[2:4] == "ls":
            pass

        # Manage changing paths
        elif command[2:4] == "cd":

            # Go back to root
            if command[5:6] == "/":
                path = "/home"

            # Go back in the path
            elif command[5:7] == "..":
                path = path[: path.rfind("/")]

            # Change path
            else:
                dirName = command[5:]  # Getting the name of new directory
                path = path + "/" + dirName  # Adding to the path
                dirs.update({path: 0})

    # Do nothing when listing directories avalible
    elif command[0:3] == "dir":
        pass

    # Get the file size and change directories in which it was found
    else:
        size = int(command[: command.find(" ")])  # Get the size of the file
        dir = path

        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[: dir.rfind("/")]


total = 0

# space required - space unused (total space - space used)
limit = 30000000 - (70000000 - dirs["/home"])
validDir = []

for dir in dirs:

    # Part 1
    if dirs[dir] <= 100000:
        total += dirs[dir]

    # Part 2
    if limit <= dirs[dir]:
        validDir.append(dirs[dir])

    smallest = min(validDir)


print("Answer to part 1: ", total)
print("Answer to part 2: ", smallest)

for dir in dirs:
    print(dir, dirs[dir])
