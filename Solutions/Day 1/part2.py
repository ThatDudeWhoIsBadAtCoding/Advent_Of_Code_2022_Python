curr = 0
elves = []

with open("calories.txt", "r") as cals:
    for i in cals.readlines():
        if i != "\n":
            curr += int(i)
        else:
            elves.append(curr)
            curr = 0

elves.sort()
print(elves[-1] + elves[-2] + elves[-3])
