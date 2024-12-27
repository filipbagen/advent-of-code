import functools

# Read and split input file into sections
with open("input.txt") as f:
    sections = f.read().strip().split('\n\n')

# Parse ordering rules from first section
rules = [list(map(int, line.split('|'))) for line in sections[0].splitlines()]

# Create cache for number comparisons
# -1 means x should come before y, 1 means y should come before x
cache = {}
for x, y in rules:
    cache[(x, y)] = -1
    cache[(y, x)] = 1


def is_ordered(nums):
    """Check if numbers are in correct order based on rules"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            key = (nums[i], nums[j])
            if key in cache and cache[key] == 1:
                return False
    return True


def cmp(x, y):
    """Compare function for sorting based on cached rules"""
    return cache.get((x, y), 0)


# Process updates and calculate total
total = 0
updates = [list(map(int, line.split(',')))
           for line in sections[1].splitlines()]

for update in updates:
    if is_ordered(update):
        continue
    # Sort numbers based on rules and add middle number to total
    update.sort(key=functools.cmp_to_key(cmp))
    total += update[len(update) // 2]

print(total)
