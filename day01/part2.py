from collections import Counter

filename = "input.txt"

with open(filename) as file:
    data = file.readlines()

    list1 = [int(ln.strip().split("   ")[0]) for ln in data]
    list2 = [int(ln.strip().split("   ")[1]) for ln in data]

counter = Counter(list2)

simm = [num * counter[num] for num in list1]

print(sum(simm))
