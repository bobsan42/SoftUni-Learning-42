games_sold = int(input())
games_list = ["Hearthstone", "Fornite", "Overwatch"]
sales_list = [0, 0, 0]
other_sales = 0
for i in range(games_sold):
    game = input()
    if game in games_list:
        idx_game = games_list.index(game)
        sales_list[idx_game] += 1
    else:
        other_sales += 1

for idx, game in enumerate(games_list):
    print(f'{game} - {(sales_list[idx] / games_sold * 100):.2f}%')

print(f'Others - {(other_sales / games_sold * 100):.2f}%')
