def some_tests():
    mylist1 = [i for i in range(11)]
    print(mylist1)

    # mylist2 = mylist1
    mylist2 = mylist1.copy()
    mylist2.pop()
    print(mylist1)
    print(mylist2)


def invert_values():
    num_string = input()
    nums_list = num_string.split(' ')
    inverted = [-int(num) for num in nums_list]
    print(inverted)


def multiples_list():
    n_factor = int(input())
    n_count = int(input())
    nums_list = [(n_factor * i) for i in range(1, n_count + 1)]
    print(nums_list)


def football_cards():
    a_team = [1 for _ in range(11)]
    b_team = [1 for _ in range(11)]
    cards_given = input()
    game_is_terminated = False

    cards_list = cards_given.split(' ')
    for current_card in cards_list:
        current_card_details = current_card.split('-')
        idx = int(current_card_details[1]) - 1
        if current_card_details[0] == 'A':
            a_team[idx] = 0
            if sum(a_team) < 7:
                game_is_terminated = True
                break
        elif current_card_details[0] == 'B':
            b_team[idx] = 0
            if sum(b_team) < 7:
                game_is_terminated = True
                break

    print(f'Team A - {sum(a_team)}; Team B - {sum(b_team)}')
    if game_is_terminated:
        print('Game was terminated')


def number_beggars():
    line_1 = input()
    beggars_count = int(input())
    offers_list = line_1.split(', ')
    beggars = [0 for _ in range(beggars_count)]
    idx = 0
    for off in offers_list:
        if idx > len(beggars) - 1:
            idx = 0
        beggars[idx] += int(off)
        idx += 1
    print(beggars)


def faro_shuffle_once(x_list):
    n = int(len(x_list) / 2)
    half_1 = x_list[:n]
    half_2 = x_list[n:]
    new_list = []
    for idx in range(n):
        new_list.append(half_1[idx])
        new_list.append(half_2[idx])
    return new_list


def faro_shuffle():
    cards_string = input()
    cards_list = cards_string.split(' ')
    shuffles_count = int(input())
    for _ in range(shuffles_count):
        cards_list = faro_shuffle_once(cards_list)
    print(cards_list)


def survival_of_the_biggest():
    numbers_string = input()
    numbers_list = numbers_string.split(' ')
    remove_count = int(input())
    while remove_count > 0 and len(numbers_list) > 0:
        # find the smallest
        min_num = int(numbers_list[0])
        for num in numbers_list:
            if int(num) < min_num:
                min_num = int(num)
        min_num = str(min_num)

        # Remove the smallest found
        # while min_num in numbers_list:
        #     numbers_list.remove(min_num)
        numbers_list.remove(min_num)
        remove_count -= 1

    numbers_string = ', '.join(numbers_list)
    print(numbers_string)


def easter_gifts():  # TODO 90/100 in JUDGE
    gifts_string = input()
    gifts_list = gifts_string.split(' ')
    command = input()
    while command != 'No Money':
        cmd_list = command.split(' ')
        gift_name = cmd_list[1]
        if cmd_list[0] == 'OutOfStock':
            for idx in range(len(gifts_list) - 1):
                if gifts_list[idx] == gift_name:
                    gifts_list[idx] = 'None'
        elif cmd_list[0] == 'Required':
            idx = int(cmd_list[-1])
            if 0 < idx < len(gifts_list):
                gifts_list[idx] = gift_name
            # gifts_list[idx] = gift_name
        elif cmd_list[0] == 'JustInCase':
            gifts_list[-1] = gift_name
        command = input()

    while 'None' in gifts_list:
        gifts_list.remove('None')
    result = ' '.join(gifts_list)
    print(result)


def seize_the_fire():
    fire_ranges = [['High', 81, 125], ['Medium', 51, 80], ['Low', 1, 50]]
    fires_input = input()
    water_amount = int(input())
    fires_data = fires_input.split('#')
    total_effort = 0
    total_fire_put_out = 0
    fire_put_out = []
    # out_of_water = False

    # split all data into lists
    for idx, data in enumerate(fires_data):
        fires_data[idx] = data.split(' = ')
        fires_data[idx][1] = int(fires_data[idx][1])

    # for i in range(len(fires_data) - 1, -1, -1):
    for i in range(0, len(fires_data)):
        fire_type = fires_data[i][0]
        cell_value = int(fires_data[i][1])
        for limits in fire_ranges:
            if limits[0] == fire_type:
                # Remove invalid fires
                if cell_value < limits[1] or cell_value > limits[2]:
                    # Cell value is not valid
                    break
                else:
                    # put out the fire if water is enough
                    if water_amount < cell_value:
                        break
                    else:
                        fire_put_out.append(cell_value)
                        water_amount -= cell_value
                        total_fire_put_out += cell_value
                        total_effort += .25 * cell_value
    print('Cells:')
    for ff in fire_put_out:
        print(f' - {ff}')
    print(f'Effort: {total_effort:.2f}')
    print(f'Total Fire: {total_fire_put_out}')


def hello_france():
    train_ticket = 150  # USD
    markup = .4  # 40%
    types_list = ['Clothes', 'Shoes', 'Accessories']
    maximum_prices = [50, 35, 20.5]
    items_bought = []
    items_prices = []
    collection_of_items = input().split('|')
    budget = float(input())
    for item in collection_of_items:
        item_type = item.split('->')[0]
        item_price = float(item.split('->')[1])
        idx = types_list.index(item_type)
        if item_price > maximum_prices[idx] or item_price > budget:
            continue
        items_bought.append(item_type)
        items_prices.append(item_price)
        budget -= item_price
    money_spent = sum(items_prices)
    profit = markup * money_spent
    budget += money_spent
    for pp in items_prices:
        print(f'{pp * 1.4:.2f}', end=' ')
    print()
    print(f'Profit: {profit:.2f}')

    if budget + profit < train_ticket:
        print('Not enough money.')
    else:
        print('Hello, France!')


def bread_factory():  # TODO 77/100 in JUDGE
    init_energy = 100
    init_coins = 100
    workday_events = input().split('|')
    energy = init_energy
    coins = init_coins
    all_events_handled = True

    for event in workday_events:
        text = event.split('-')[0]
        number = int(event.split('-')[1])
        if text == 'rest':
            gain = min(number, init_energy - energy)
            energy += gain
            print(f'You gained {gain} energy.')
            print(f'Current energy: {energy}.')
        elif text == 'order':
            if energy >= 30:
                energy -= 30
                coins += number
                print(f'You earned {number} coins.')
            else:
                energy += 50
                print('You had to rest!')
                all_events_handled = False
        else:
            if number > coins:
                print(f'Closed! Cannot afford {text}.')
                all_events_handled = False
                break
            else:
                coins -= number
                print(f'You bought {text}.')

    if all_events_handled:
        print('Day completed!')
        print(f'Coins: {coins}')
        print(f'Energy: {energy}')


def bread_factory_v2_ivanshopov():
    list_of_events = input().split('|')
    total_energy = 100
    total_coins = 100
    bakery_is_open = True
    for event in list_of_events:
        event_info = event.split('-')
        type_of_event= event_info[0]
        number = int(event_info[1])
        if type_of_event=='rest':
            temporary_energy = total_energy
            total_energy +=number
            if total_energy>100:
                total_energy=100
            gained_energy =total_energy - temporary_energy
            print(f'You gained {gained_energy} energy.')
            print(f'Current energy: {total_energy}.')
        elif type_of_event=='order':
            if total_energy>=30:
                total_energy -= 30
                total_coins += number
                print(f'You earned {number} coins.')
            else:
                total_energy+= 50
                # if total_energy > 100:
                #     total_energy = 100
                print('You had to rest!')
        else:
            if total_coins>= number:
                total_coins -= number
                print(f'You bought {type_of_event}.')
            else:
                print(f'Closed! Cannot afford {type_of_event}.')
                bakery_is_open = False
                break
    if bakery_is_open:
        print('Day completed!')
        print(f'Coins: {total_coins}')
        print(f'Energy: {total_energy}')

######################################################################
# RUN time
######################################################################
# invert_values()
# multiples_list()
# football_cards()
# number_beggars()
# faro_shuffle()
# survival_of_the_biggest()
# easter_gifts()
# seize_the_fire()
# hello_france()
# bread_factory()
bread_factory_v2_ivanshopov()