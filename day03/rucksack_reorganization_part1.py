import os

with open("input.txt") as f:
    data = f.read()
    arr = data.split("\n")

    total = 0
    for line in arr:
        first_half, second_half = line[:len(line)//2], line[len(line)//2:]
        common_character = ''.join(set(first_half).intersection(set(second_half)))
        if common_character >= 'a':
            total += ord(common_character) - ord('a') + 1
        else:
            total += ord(common_character) - ord('A') + 27

print(total)