with open("input.txt") as f:
    lines = f.read().splitlines()


def isValid(x: int, y: int, sizeX: int, sizeY: int) -> bool:
    return 0 <= x < sizeX and 0 <= y < sizeY


def findWordInDirection(grid: list, n: int, m: int, word: str, index: int,
                        x: int, y: int, dirX: int, dirY: int) -> bool:
    if index == len(word):
        return True

    if isValid(x, y, n, m) and word[index] == grid[x][y]:
        return findWordInDirection(grid, n, m, word, index + 1,
                                   x + dirX, y + dirY, dirX, dirY)

    return False


grid = [list(line) for line in lines]
word = "XMAS"

occurance = 0
n, m = len(grid), len(grid[0])

# Directions for 8 possible movements
directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
              (1, 1), (1, -1), (-1, 1), (-1, -1)]

for i in range(n):
    for j in range(m):
        # Check if the first character matches
        if grid[i][j] == word[0]:
            for dirX, dirY in directions:
                if findWordInDirection(grid, n, m, word, 0,
                                       i, j, dirX, dirY):
                    occurance += 1

print(occurance)
