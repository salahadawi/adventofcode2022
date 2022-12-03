import os

with open("input.txt") as f:
    data = f.read()
    arr = data.split("\n")

    total = 0
    for line in arr:
        my_round_score = 0
        if line[2] == "Y":
            my_round_score += 3
        elif line[2] == "Z":
            my_round_score += 6

        opponent_round_score = ord(line[0]) - ord("@")

        if opponent_round_score == 1:
            if my_round_score == 0:
                total += 3
            elif my_round_score == 3:
                total += 1
            elif my_round_score == 6:
                total += 2
        elif opponent_round_score == 2:
            if my_round_score == 0:
                total += 1
            elif my_round_score == 3:
                total += 2
            elif my_round_score == 6:
                total += 3
        elif opponent_round_score == 3:
            if my_round_score == 0:
                total += 2
            elif my_round_score == 3:
                total += 3
            elif my_round_score == 6:
                total += 1

        total += my_round_score

print(total)
