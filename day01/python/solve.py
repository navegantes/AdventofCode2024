import os
from collections import Counter

current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)

filename = "input.txt"
filepath = os.path.join(parent_directory, "data", filename)

with open(filepath) as file:
    data = file.readlines()

    list1 = [int(ln.strip().split("   ")[0]) for ln in data]
    list2 = [int(ln.strip().split("   ")[1]) for ln in data]

# Part 1
list1.sort()
list2.sort()

diff = [abs(ln1 - ln2) for ln1, ln2 in zip(list1, list2)]

print(sum(diff))

# Part 2
counter = Counter(list2)
simm = [num * counter[num] for num in list1]

print(sum(simm))