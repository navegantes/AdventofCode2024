import os


def get_file(filename):
    parent_directory = os.path.dirname(os.path.dirname(__file__))
    base_dir = os.path.dirname(parent_directory)

    return os.path.join(base_dir, "data", filename)


def is_valid(level):
    diffs = [level[i + 1] - level[i] for i, _ in enumerate(level) if i < len(level) - 1]
    signal = diffs[0] > 0

    for val in diffs:
        if abs(val) > 0 and abs(val) <= 3:
            valid = True
        else:
            valid = False
            break

        if (val > 0) == signal:
            valid = True
        else:
            valid = False
            break

    return valid


def is_valid_dampener(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1 :]
        if is_valid(modified_levels):
            return True


filename = "reports.txt"
filepath = get_file(filename)

with open(get_file(filepath), "r") as file:
    data = file.readlines()
    reports = [[int(ln) for ln in line.strip().split(" ")] for line in data]

# part 1
count = 0
for level in reports:
    if is_valid(level):
        count += 1

print("Safe Reports - 1: ", count)

# part 2
count = 0
for level in reports:
    if is_valid_dampener(level):
        count += 1

print("Safe Reports - 2: ", count)
