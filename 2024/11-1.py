def update_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)

        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            mid = len(stone_str) // 2
            new_stones.append(int(stone_str[:mid]))
            new_stones.append(int(stone_str[mid:]))

        else:
            new_stones.append(stone * 2024)

    return new_stones


with open('input.txt') as f:
    stones = [int(x) for x in f.read().split()]

BLINKS = 25

for i in range(BLINKS):
    stones = update_stones(stones)

print(len(stones))
