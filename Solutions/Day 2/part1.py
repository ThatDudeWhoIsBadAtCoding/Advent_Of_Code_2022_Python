bonus_rock = 1
bonus_paper = 2
bonus_scissors = 3
win_points = 6
draw_points = 3
loss_points = 0
score = 0


def check_winner(opponent_choice: str, your_choice: str) -> int:
    if opponent_choice == "A" and your_choice == "X":
        return draw_points + bonus_rock
    if opponent_choice == "B" and your_choice == "Y":
        return draw_points + bonus_paper
    if opponent_choice == "C" and your_choice == "Z":
        return draw_points + bonus_scissors
    if opponent_choice == "A" and your_choice == "Y":
        return win_points + bonus_paper
    if opponent_choice == "B" and your_choice == "Z":
        return win_points + bonus_scissors
    if opponent_choice == "C" and your_choice == "X":
        return win_points + bonus_rock
    # must be a loss now
    if your_choice == "X":
        return loss_points + bonus_rock
    if your_choice == "Y":
        return loss_points + bonus_paper
    return loss_points + bonus_scissors


with open("Day 2/guide.txt", "r") as guide:
    for match in guide.readlines():
        curr_match = match.split(" ")
        curr_match[1] = curr_match[1].removesuffix("\n")
        curr_score = check_winner(curr_match[0], curr_match[1])
        score += curr_score

print(score)
