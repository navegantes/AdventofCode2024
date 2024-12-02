filename = "input.txt"

with open(filename) as file:
    data = file.readlines()

    list1 = [int(ln.strip().split("   ")[0]) for ln in data]
    list2 = [int(ln.strip().split("   ")[1]) for ln in data]

list1.sort()
list2.sort()

diff = [abs(ln1 - ln2) for ln1, ln2 in zip(list1, list2)]

print(sum(diff))
