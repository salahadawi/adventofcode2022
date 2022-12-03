import os

with open("input.txt") as f:
    data = f.read()
    arr = data.split("\n")

    total = 0
    for line in arr:
        my_round_score = ord(line[2]) - ord("W")
        opponent_round_score = ord(line[0]) - ord("@")

        if my_round_score == opponent_round_score:
            total += 3
        elif my_round_score == 1:
            if opponent_round_score == 3:
                total += 6
        elif my_round_score == 2:
            if opponent_round_score == 1:
                total += 6
        elif my_round_score == 3:
            if opponent_round_score == 2:
                total += 6

        total += my_round_score

print(total)
