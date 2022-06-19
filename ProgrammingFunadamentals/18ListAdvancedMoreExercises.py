def social_distribution():
    population_wealth = input().split(', ')
    min_wealth = int(input())
    distribution = list(map(int, population_wealth))
    # equality_impossible = False
    equality_impossible = (sum(distribution) < len(distribution) * min_wealth)
    if equality_impossible:
        print('No equal distribution possible')
        return

    for idx, wealth in enumerate(distribution):
        # if equality_impossible:
        #     break
        if min(distribution) >= min_wealth:
            break
        while distribution[idx] < min_wealth:
            richest = max(distribution)
            # if richest <= min_wealth:
            #     equality_impossible = True
            #     break
            rich_idx = distribution.index(richest)
            distribution[idx] += 1
            distribution[rich_idx] -= 1
    print(distribution)


def social_distribution_logic2():
    population_wealth = input().split(', ')
    min_wealth = int(input())
    distribution = list(map(int, population_wealth))
    # equality_impossible = False
    equality_impossible = (sum(distribution) < len(distribution) * min_wealth)
    if equality_impossible:
        print('No equal distribution possible')
        return

    for idx, wealth in enumerate(distribution):
        # if equality_impossible:
        #     break
        if min(distribution) >= min_wealth:
            break
        while distribution[idx] < min_wealth:
            richest = max(distribution)
            # if richest <= min_wealth:
            #     equality_impossible = True
            #     break
            rich_idx = distribution.index(richest)
            money_needed = min_wealth - distribution[idx]
            money_available = distribution[rich_idx] - min_wealth
            money_to_transfer = min(money_needed, money_available)

            distribution[idx] += money_to_transfer
            distribution[rich_idx] -= money_to_transfer
    print(distribution)


def take_skip_rope():
    input_string = list(input())
    numbers_list = [x for x in input_string if ord('0') <= ord(x) <= ord('9')]
    symbols_list = [x for x in input_string if (ord(x) < ord('0') or ord(x) > ord('9'))]
    take_list = list(map(int, numbers_list[::2]))
    skip_list = list(map(int, numbers_list[1::2]))
    # •	The count of digits in the input string will always be even.
    # •	The encrypted message will contain any printable ASCII character.
    result = ''
    current_position = 0
    for i in range(len(take_list)):
        for char in symbols_list[current_position:current_position + take_list[i]]:
            result += char
        current_position += take_list[i] + skip_list[i]
    print(result)


def battleships():
    battlefield = []
    ships_destroyed = 0
    n_rows = int(input())

    for _ in range(n_rows):
        row = input().split()
        row = list(map(int, row))
        battlefield.append(row)

    attacks_list = input().split()
    for attack in attacks_list:
        coordinates = list(map(int, attack.split('-')))
        x = battlefield[coordinates[0]][coordinates[1]]
        if x > 0:
            x -= 1
            if x == 0:
                ships_destroyed += 1
        battlefield[coordinates[0]][coordinates[1]] = x

    print(ships_destroyed)


# Driver code
if __name__ == '__main__':
    # function call
    # social_distribution()
    # social_distribution_logic2()
    # take_skip_rope()
    battleships()
