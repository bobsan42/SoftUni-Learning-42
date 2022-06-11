winner_name = ""
winner_score = 0

player_name = input()
while player_name != "Stop":
    name_length = len(player_name)
    player_score = 0
    for letter in player_name:
        guess_number = int(input())
        if guess_number == ord(letter):
            player_score += 10
        else:
            player_score += 2

    if player_score >= winner_score:
        winner_score = player_score
        winner_name = player_name

    player_name = input()

print(f'The winner is {winner_name} with {winner_score} points!')
