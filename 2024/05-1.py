# Read and split input file into sections
with open("input.txt") as f:
    page_ordering_rules, updates = f.read().strip().split('\n\n')

# Parse rules from first section
rules = [list(map(int, line.split('|'))) for line in page_ordering_rules.splitlines()]

# Create cache for comparing number pairs
# cache[(x,y)] = True means x should come before y
cache = {(x, y): True for x, y in rules}
cache.update({(y, x): False for x, y in rules})

def is_ordered(nums):
    """Check if numbers are in correct order based on rules"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i], nums[j]) in cache and not cache[(nums[i], nums[j])]:
                return False
    return True

# Process updates and calculate total
total = 0
updates = [list(map(int, line.split(','))) for line in updates.splitlines()]

for update in updates:
    if is_ordered(update):
        # If ordered, add middle number to total
        total += update[len(update) // 2]

print(total)