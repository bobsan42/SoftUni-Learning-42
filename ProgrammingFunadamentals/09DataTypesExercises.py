def integer_operations():
    numbers_list = []
    for _ in range(4):
        i = int(input())
        numbers_list.append(i)
    result = ((numbers_list[0] + numbers_list[1]) // numbers_list[2]) * numbers_list[3]
    print(result)


def chars_to_string():
    result = ''
    for _ in range(3):
        result += input()
    print(result)


def elevator():
    persons = int(input())
    capacity = int(input())
    trips = persons // capacity
    if persons % capacity > 0:
        trips += 1
    print(trips)


def elevator_v2():
    from math import ceil
    persons = int(input())
    capacity = int(input())
    trips = ceil(persons / capacity)
    print(trips)


def sum_of_chars():
    char_count = int(input())
    total_sum = 0
    for _ in range(char_count):
        total_sum += ord(input())
    print(f'The sum equals: {total_sum}')


def print_part_ascii_table():
    idx_start = int(input())
    idx_end = int(input())
    for i in range(idx_start, idx_end + 1):
        print(chr(i), end=' ')


def triples_of_letters():
    idx_a = ord('a')
    used_letters = int(input())
    for i in range(used_letters):
        for j in range(used_letters):
            for k in range(used_letters):
                print(f'{chr(idx_a + i)}{chr(idx_a + j)}{chr(idx_a + k)}')


def water_overflow():
    tank_capacity = 255
    remaining_capacity = tank_capacity
    n = int(input())
    for _ in range(n):
        qty_to_add = int(input())
        if qty_to_add > remaining_capacity:
            print('Insufficient capacity!')
            continue
        remaining_capacity -= qty_to_add
    print(tank_capacity - remaining_capacity)


def party_profit():
    from math import floor
    group_size = int(input())
    adventure_days = int(input())
    coins = 0
    for i in range(1, adventure_days + 1):
        if i % 10 == 0:
            group_size -= 2
        if i % (3 * 5) == 0:
            group_size += 5
        coins += 50
        coins -= 2 * (group_size)
        if i % 3 == 0:
            coins -= 3 * (group_size)
        if i % 5 == 0:
            coins += 20 * (group_size)
        if i % (3 * 5) == 0:
            coins -= 2 * (group_size)
    print(f"{group_size} companions received {floor(coins / group_size)} coins each.")


def snowballs():
    n_snowballs = int(input())
    best_snowball_data = [0, 0, 0, None]
    for _ in range(n_snowballs):
        sb_weight = int(input())
        sb_time = int(input())
        sb_quality = int(input())
        sb_value = round((sb_weight / sb_time) ** sb_quality)
        if (best_snowball_data[3] is None) or (best_snowball_data[3] < sb_value):
            best_snowball_data[0] = sb_weight
            best_snowball_data[1] = sb_time
            best_snowball_data[2] = sb_quality
            best_snowball_data[3] = sb_value

    print(f'{best_snowball_data[0]} : {best_snowball_data[1]} = {best_snowball_data[3]} ({best_snowball_data[2]})')


def gladiator_expenses():
    lost_fights_count = int(input())
    helmet_price = float(input())
    sword_price = float(input())
    shield_price = float(input())
    armor_price = float(input())
    expenses = 0

    for i in range(1, lost_fights_count + 1):
        if i % 2 == 0:
            expenses += helmet_price
        if i % 3 == 0:
            expenses += sword_price
        if i % (2 * 3) == 0:
            expenses += shield_price
            if i % (2 * 2 * 3) == 0:
                expenses += armor_price

    print(f'Gladiator expenses: {expenses:.2f} aureus')


################################################
# RUN!
###########################################
gladiator_expenses()
