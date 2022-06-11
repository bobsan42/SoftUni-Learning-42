team_name = input()
games_played = int(input())

games_won = 0
games_draw = 0
games_lost = 0

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
    exit()

for i in range(games_played):
    result = input()
    if result == "W":
        games_won += 1
    elif result == "D":
        games_draw += 1
    elif result == "L":
        games_lost += 1

total_score = games_won * 3 + games_draw * 1 + games_lost * 0

print(f"{team_name} has won {total_score} points during this season.")
print(f"Total stats:")
print(f"## W: {games_won}")
print(f"## D: {games_draw}")
print(f"## L: {games_lost}")
print(f"Win rate: {(games_won / games_played * 100):.2f}%")
