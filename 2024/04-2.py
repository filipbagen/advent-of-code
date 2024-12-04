with open("input.txt") as f:
    lines = f.read().splitlines()


# Valid patterns for X formation around 'A'
finds = [[['M', 'M'], ['S', 'S']],
         [['M', 'S'], ['M', 'S']],
         [['S', 'S'], ['M', 'M']],
         [['S', 'M'], ['S', 'M']]]

occurance = 0
found = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        # Look for center 'A'
        if lines[i][j] == 'A':
            # Ensure we can check all corners (not at edges)
            if (i < (len(lines) - 1) and j < (len(lines[0]) - 1)) and (i > 0 and j > 0):
                # Check if corners form valid X pattern
                corners = [
                    [lines[i-1][j-1], lines[i-1][j+1]],  # top corners
                    [lines[i+1][j-1], lines[i+1][j+1]]   # bottom corners
                ]
                if corners in finds:
                    occurance += 1

print(occurance)
