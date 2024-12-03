with open("input.txt") as f:
    reports = f.read().splitlines()


def is_safe(report: list[int]) -> bool:
    # Compute differences
    deltas = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check monotonicity
    if all(d >= 1 for d in deltas) or all(d <= -1 for d in deltas):
        # Check difference constraint
        if all(1 <= abs(d) <= 3 for d in deltas):
            return True


safe = 0


# Check each report
for report in reports:
    # Convert to integers
    report = [int(x) for x in report.split()]

    if is_safe(report):
        safe += 1
        continue

    # Brute force removing each level
    # to see if the row becomes safe
    for i in range(len(report)):
        new_row = report[:i] + report[i + 1:]
        if is_safe(new_row):
            safe += 1
            break


print(safe)
