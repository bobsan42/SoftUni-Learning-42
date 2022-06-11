n_eggs_player1 = int(input())
n_eggs_player2 = int(input())

command = input()  # winner one or two
eggs_over = False

while command != 'End of battle':
    if command == "one":
        n_eggs_player2 -= 1
    elif command == "two":
        n_eggs_player1 -= 1
    if n_eggs_player2 * n_eggs_player1 == 0:
        eggs_over = True
        break
    command = input()

if eggs_over:
    if n_eggs_player1 == 0:
        print(f'Player one is out of eggs. Player two has {n_eggs_player2} eggs left.')
    elif n_eggs_player2 == 0:
        print(f'Player two is out of eggs. Player one has {n_eggs_player1} eggs left.')
else:
    print(f'Player one has {n_eggs_player1} eggs left.')
    print(f'Player two has {n_eggs_player2} eggs left.')
