def number_definer():
    result = ''
    number = float(input())
    if number == 0:
        result = 'zero'
    else:
        if number > 0:
            result = 'positive'
        else:
            result = 'negative'

        if abs(number) < 1:
            result = 'small ' + result
        elif abs(number) > 1000000:
            result = 'large ' + result

    print(result)


def Largest_Of_Three():
    largest_number = ''
    for i in range(0, 3):
        number = int(input())
        if largest_number == '':
            largest_number = number
        else:
            largest_number = max(largest_number, number)
    print(largest_number)


def word_reverse():
    word = input()
    rev_word = ''
    for i in range(len(word) - 1, -1, -1):
        rev_word += word[i]
    print(rev_word)


def word_reverse_ver2():
    word = input()
    print(word[::-1])


def even_numbers():
    n = int(input())
    is_odd = False
    number = ''
    for i in range(0, n):
        number = int(input())
        if number % 2 == 1:
            is_odd = True
            break

    if is_odd:
        print(f'{number} is odd!')
    else:
        print('All numbers are even.')


def numbers_1_to_100():
    number = 0  # float(input())
    while number < 1 or number > 100:
        number = float(input())
    print(f'The number {number} is between 1 and 100')


def shopping():
    budget = int(input())
    money_left = budget
    command = input()
    while command != 'End':
        money_left -= int(command)
        if money_left < 0:
            print('You went in overdraft!')
            break
        command = input()
    else:
        print('You bought everything needed.')
        # exit()


def patterns():
    n_stars = int(input())
    for i in range(1, n_stars + 1):
        print('*' * i)
        # for j in range(0, i):
        #     print('*', end='')
        # print()
    for i in range(n_stars - 1, 0, -1):
        print('*' * i)
        # for j in range(0, i):
        #     print('*', end='')
        # print()


# 01
# number_definer()
# 02
# Largest_Of_Three()
# 03
# word_reverse()
# 04
# even_numbers()
# 05
# numbers_1_to_100()
# 06
# shopping()
# 07
patterns()
