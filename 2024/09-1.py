# Read and process the input
with open('input.txt') as f:
    disk_map = f.read().strip()

counter = 0
hard_disk = []

# Build the hard_disk array
for index, char in enumerate(disk_map):
    number = int(char)
    if index % 2 == 0:
        hard_disk.extend([str(counter)] * number)
        counter += 1
    else:
        hard_disk.extend(['.'] * number)

# Locate the rightmost non-dot and the leftmost dot for swapping
right_idx = len(hard_disk) - 1
left_idx = 0

while right_idx > left_idx:
    # Find the rightmost non-dot
    while right_idx >= 0 and hard_disk[right_idx] == '.':
        right_idx -= 1
    # Find the leftmost dot
    while left_idx < len(hard_disk) and hard_disk[left_idx] != '.':
        left_idx += 1
    # Swap if valid indices are found
    if right_idx > left_idx:
        hard_disk[right_idx], hard_disk[left_idx] = hard_disk[left_idx], hard_disk[right_idx]

# Filter out dots and calculate checksum
checksum = 0
position = 0
for char in hard_disk:
    if char != '.':
        checksum += position * int(char)
        position += 1

print(checksum)
