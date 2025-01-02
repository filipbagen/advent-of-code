def update_stone(stone):

    if stone == 0:
        return [1]

    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        mid = len(stone_str) // 2
        return [int(stone_str[:mid]), int(stone_str[mid:])]

    return [stone * 2024]


with open('input.txt') as f:
    stones = {int(x): 1 for x in f.read().split()}

BLINKS = 75

for _ in range(BLINKS):
    new_stones = {}
    for stone, count in stones.items():
        for new_stone in update_stone(stone):
            new_stones[new_stone] = new_stones.get(new_stone, 0) + count
    stones = new_stones  # Update stones for next iteration

print(f"Total stones after {BLINKS} blinks: {sum(stones.values())}")
