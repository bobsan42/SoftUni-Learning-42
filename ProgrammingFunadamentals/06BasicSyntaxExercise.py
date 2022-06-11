def jenny_message():
    username = input()
    if username != 'Johnny':
        print(f'Hello, {username}!')
    else:
        print(f'Hello, my love!')


def drink_something():
    age = int(input())
    if age <= 14:
        print('drink toddy')
    elif age <= 18:
        print('drink coke')
    elif age <= 21:
        print('drink beer')
    else:
        print('drink whisky')


def chat_codes():
    n_messages = int(input())
    chat_code = 0
    for i in range(0, n_messages):
        chat_code = int(input())
        if chat_code == 88:
            print("Hello")
        elif chat_code == 86:
            print('How are you?')
        elif chat_code < 88:
            print('GREAT!')
        elif chat_code > 88:
            print('Bye.')


def max_multiple():
    divisor = int(input())
    boundary = int(input())
    result = 0
    if boundary >= divisor:
        result = boundary - (boundary % divisor)
    print(result)


def coffee_orders():
    n_orders = int(input())
    total_price = 0.0
    for i in range(0, n_orders):
        price_per_capsule = float(input())
        n_days = int(input())
        capsules_per_day = int(input())
        if not (0.01 <= price_per_capsule <= 100):
            continue
        if not (1 <= n_days <= 31):
            continue
        if not (1 <= capsules_per_day <= 2000):
            continue
        coffee_price = price_per_capsule * n_days * capsules_per_day
        print(f'The price for the coffee is: ${coffee_price:.2f}')
        total_price += coffee_price
    print(f'Total: ${total_price:.2f}')


def string_pureness():
    n_strings = int(input())
    for i in range(0, n_strings):
        str_input = input()
        for letter in str_input:
            if letter == ',' or letter == '.' or letter == '_':
                print(f'{str_input} is not pure!')
                break
        else:
            print(f'{str_input} is pure.')


def string_pureness_ver2():
    n_strings = int(input())
    for i in range(0, n_strings):
        str_input = input()
        if ',' in str_input or '.' in str_input or '_' in str_input:
            print(f'{str_input} is not pure!')
        else:
            print(f'{str_input} is pure.')


def double_char():
    str_input = input()
    while str_input != 'End':
        result = ''
        if str_input != 'SoftUni':
            for a in str_input:
                result += a * 2
            print(result)
        str_input = input()


def how_much_coffee():
    command = input()
    coffee_needed = 0
    while command != 'END':
        if command.lower() == 'coding' or \
                command.lower() == 'dog' or \
                command.lower() == 'cat' or \
                command.lower() == 'dog' or \
                command.lower() == 'movie':
            if command.lower() == command:
                coffee_needed += 1
            elif command.upper() == command:
                coffee_needed += 2
        command = input()

    if coffee_needed > 5:
        print('You need extra sleep')
    else:
        print(coffee_needed)


def sorting_hat():
    student_name = input()
    while student_name != 'Welcome!':
        if student_name == 'Voldemort':
            print('You must not speak of that name!')
            break
        home_name = ''
        if len(student_name) < 5:
            home_name = 'Gryffindor'
        elif len(student_name) == 5:
            home_name = 'Slytherin'
        elif len(student_name) == 6:
            home_name = 'Ravenclaw'
        elif len(student_name) > 5:
            home_name = 'Hufflepuff'
        print(f'{student_name} goes to {home_name}.')
        student_name = input()
    else:
        print('Welcome to Hogwarts.')


def mutate_strings():
    first_string = input()
    second_string = input()
    len_str = len(first_string)
    for i in range(0, len_str):
        if first_string[i] == second_string[i]:
            continue
        mutation = ''
        for j in range(0, i + 1):
            mutation += second_string[j]
        for j in range(i + 1, len_str):
            mutation += first_string[j]
        print(mutation)


def easter_bread():
    budget = float(input())
    price_flour = float(input())
    # 1 loaf of bread recipe:
    # Eggs - 1 pack
    # Flour - 1 pack
    # Milk - 250 ml
    price_eggs = .75 * price_flour
    price_milk = 1.25 * price_flour
    count_colored_eggs = 0
    count_loaves = 0
    loaf_cost = price_eggs + price_flour + price_milk * .25
    while budget >= loaf_cost:
        budget -= loaf_cost
        count_loaves += 1
        count_colored_eggs += 3
        if count_loaves % 3 == 0:
            count_colored_eggs -= count_loaves - 2

    print(
        f'You made {count_loaves} loaves of Easter bread! Now you have {count_colored_eggs} eggs and {budget:.2f}BGN left.')


def christmas_spirit():
    qty_decorations_per_shopping = int(input())
    days_left_to_xmas = int(input())
    total_cost = 0
    total_spirit = 0
    if days_left_to_xmas % 10 == 0:  # cat problems
        total_spirit -= 30

    for i in range(1, days_left_to_xmas + 1):
        if i % 11 == 0:  # cat problems
            qty_decorations_per_shopping += 2

        if i % 2 == 0:
            total_cost += qty_decorations_per_shopping * 2
            total_spirit += 5
        if i % 3 == 0:
            total_cost += qty_decorations_per_shopping * (5 + 3)
            total_spirit += 3 + 10
        if i % 5 == 0:
            total_cost += qty_decorations_per_shopping * 15
            total_spirit += 17
        if i % 15 == 0:
            total_spirit += 30

        if i % 10 == 0:  # cat problems
            total_spirit -= 20
            total_cost += 5 + 3 + 15

    print(f'Total cost: {total_cost}')
    print(f'Total spirit: {total_spirit}')


################################################
# RUN!
###########################################
string_pureness_ver2()
