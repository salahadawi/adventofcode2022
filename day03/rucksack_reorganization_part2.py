import os

with open("input.txt") as f:
    data = f.read()
    arr = data.split("\n")

    total = 0
    for i in range(0, len(arr), 3):
        common_character = ''.join(set.intersection(*map(set, arr[i:i + 3])))
        if common_character >= 'a':
            total += ord(common_character) - ord('a') + 1
        else:
            total += ord(common_character) - ord('A') + 27

print(total)