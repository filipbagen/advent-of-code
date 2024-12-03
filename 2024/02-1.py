with open("input.txt") as f:
    reports = f.read().splitlines()

safe = 0

for report in reports:
    # Convert to integers
    report = [int(x) for x in report.split()]

    # Compute differences
    deltas = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check monotonicity
    if all(d >= 1 for d in deltas) or all(d <= -1 for d in deltas):
        # Check difference constraint
        if all(1 <= abs(d) <= 3 for d in deltas):
            safe += 1

print(safe)
