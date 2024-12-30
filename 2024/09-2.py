# Read and process the input
with open('input.txt') as f:
    disk_map = f.read().strip()

# Pre-calculate sizes and positions for more efficient processing
file_sizes = []
file_positions = []
total_size = 0

# First pass - calculate sizes and initial positions
for index, char in enumerate(disk_map):
    size = int(char)
    total_size += size
    if index % 2 == 0:
        file_sizes.append(size)
        file_positions.append(total_size - size)

# Create hard disk with exact size needed
hard_disk = ['.'] * total_size
current_pos = 0

# Initialize disk with files
for file_id, (size, pos) in enumerate(zip(file_sizes, file_positions)):
    for i in range(pos, pos + size):
        hard_disk[i] = str(file_id)

# Process files from highest to lowest ID
max_file_id = len(file_sizes) - 1

while max_file_id >= 0:
    file_id_str = str(max_file_id)
    file_size = file_sizes[max_file_id]

    # Find current file position (only search in relevant range)
    start_pos = 0
    while start_pos < len(hard_disk) and hard_disk[start_pos] != file_id_str:
        start_pos += 1

    # Skip if file is already at the leftmost possible position
    if start_pos == 0:
        max_file_id -= 1
        continue

    # Count free spaces from the beginning
    free_start = 0
    while free_start < start_pos:
        # Quick check if moving would be beneficial
        if free_start >= start_pos:
            break

        # Count consecutive free spaces
        free_end = free_start
        while free_end < start_pos and hard_disk[free_end] == '.':
            free_end += 1

        free_length = free_end - free_start

        # Move file if enough space is found
        if free_length >= file_size:
            # Batch move operations instead of one by one
            new_section = [file_id_str] * file_size
            old_section = ['.'] * file_size

            # Use slice assignment for faster operations
            hard_disk[free_start:free_start + file_size] = new_section
            hard_disk[start_pos:start_pos + file_size] = old_section
            break

        free_start = free_end + 1

    max_file_id -= 1

# Calculate checksum more efficiently
checksum = 0
for pos, val in enumerate(hard_disk):
    if val != '.':
        checksum += pos * int(val)

print(checksum)
