def concat_names():
    first_name = input()
    last_name = input()
    delimiter = input()

    print(f'{first_name}{delimiter}{last_name}')


def convert_meters_to_kilometers():
    meters = int(input())
    print(f'{(meters / 1000):.2f}')


def pounds_to_dollars():
    pounds = int(input())
    dollars = pounds * 1.31
    print(f'{dollars:.3f}')


def centuries_to_minutes():
    centuries = int(input())
    years = centuries * 100
    days = int(years * 365.2422)
    hours = days * 24
    minutes = hours * 60
    print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')


def special_numbers():
    n = int(input())
    special_numbers_list = [5, 7, 11]
    for i in range(1, n + 1):
        print(f'{i} -> ', end='')
        number = i
        sum_of_digits = 0
        while number > 0:
            sum_of_digits += number % 10
            number = number // 10
        if sum_of_digits in special_numbers_list:
            print(True)
        else:
            print(False)


def next_happy_year():
    given_year = int(input())
    is_happy = False
    year = given_year
    while not is_happy:
        year += 1
        year_string = str(year)
        for char in year_string:
            if year_string.count(char) > 1:
                break
        else:
            is_happy = True
    print(year)


def next_happy_year_v2():
    from itertools import permutations
    digits_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number = tuple(map(int, input()))
    my_perm = permutations(digits_list, len(number))
    for digits in list(my_perm):
        if digits > number:
            result = ''.join(str(x) for x in digits)
            print(result)
            break


################################################
# RUN!
###########################################
next_happy_year_v2()
