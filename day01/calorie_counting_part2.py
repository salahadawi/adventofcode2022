import os

with open("input.txt") as f:
    data = f.read()
    arr = data.split("\n\n")

    sums = []
    for line in arr:
        sums.append(sum(list(map(int, line.split("\n")))))

sums.sort(reverse=True)
print(sum(sums[0:3]))