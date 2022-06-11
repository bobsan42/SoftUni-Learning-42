# problem 1
import math


def smallest_of_three_numbers():
    numbers = []
    for _ in range(3):
        numbers.append(int(input()))

    result = min(numbers)
    print(result)


# problem 2
def add_and_subtract(a, b, c):
    def sum_numbers():
        return a + b

    def subtract():
        return sum_numbers() - c

    print(subtract())


def problem_2():
    a = int(input())
    b = int(input())
    c = int(input())
    add_and_subtract(a, b, c)


# problem 3
def characters_in_range():
    from_char = input()
    to_char = input()

    def print_char(i: int):
        if i < ord(to_char):
            print(chr(i), end=' ')
            print_char(i + 1)
        else:
            print()

    print_char(ord(from_char) + 1)


def characters_in_range_v2():
    from_char = input()
    to_char = input()
    collected_chars = []
    for n_ascii in range(ord(from_char) + 1, ord(to_char)):
        collected_chars.append(chr(n_ascii))
    # print(*collected_chars)
    print(*collected_chars, sep=' ')


# problem 4
def odd_and_even_sum():
    given_number = input()
    digits = list(map(int, list(given_number)))
    sum_odds = sum(list(filter(lambda x: x % 2 != 0, digits)))  # odds only
    sum_evens = sum(list(filter(lambda x: x % 2 == 0, digits)))  # evens only
    print(f'Odd sum = {sum_odds}, Even sum = {sum_evens}')


# problem 5
def even_numbers():
    given_numbers = input()
    numbers = list(map(int, given_numbers.split()))
    result = list(filter(lambda x: x % 2 == 0, numbers))  # evens only
    print(result)
    exit()
    # version 2 - list comprehension
    result = [int(s) for s in given_numbers.split() if s % 2 == 0]


# problem 6
def sorting():
    given_numbers = input()
    numbers = list(map(int, given_numbers.split()))
    result = sorted(numbers)
    print(result)


# problem 7
def min_max_sum():
    given_numbers = input()
    numbers = list(map(int, given_numbers.split()))

    print(f"The minimum number is {min(numbers)}")
    print(f"The maximum number is {max(numbers)}")
    print(f"The sum number is: {sum(numbers)}")


# problem 8
def palindrome_integers():
    given_numbers = input()
    numbers = given_numbers.split(', ')

    def is_palindrome(num: str):
        return num == num[::-1]

    for x in numbers:
        print(is_palindrome(x))


# problem 9
def password_validator(password: str):
    isValid = True
    not_allowed_characters = False
    count_digits = 0
    # check length
    x = len(password)
    if x < 6 or x > 10:
        print('Password must be between 6 and 10 characters')
        isValid = False
    for letter in password:
        x = ord(letter)
        if (x not in range(ord('0'), ord('9') + 1)) and \
                (x not in range(ord('A'), ord('Z') + 1)) and \
                (x not in range(ord('a'), ord('z') + 1)):
            not_allowed_characters = True
        if x in range(ord('0'), ord('9') + 1):
            count_digits += 1
    if not_allowed_characters:
        isValid = False
        print('Password must consist only of letters and digits')
    if count_digits < 2:
        isValid = False
        print('Password must have at least 2 digits')
    if isValid:
        print('Password is valid')


# problem 10
def find_divisors(num: int):
    divisors = []
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            j = num / i
            if i not in divisors:
                divisors.append(i)
                divisors.append(j)
    return divisors


def perfect_number(number):
    divs = find_divisors(number)
    divs.remove(number)
    aliquot_sum = sum(divs)
    if number == aliquot_sum:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


# problem 11 *
def loading_bar(num: int):
    total_num = 100
    number_of_bars = 10
    is_complete = False
    percent_complete = int(num / total_num * 100)
    bars_complete = int(percent_complete / number_of_bars)

    if num == total_num:
        print('100% Complete!')
        print('[' + '%' * number_of_bars + ']')
    else:
        print(str(percent_complete) + '% [' + '%' * bars_complete + '.' * (number_of_bars - bars_complete) + ']')
        print('Still loading...')


# problem 12 *

def factorial_division():
    num1 = int(input())
    num2 = int(input())
    fact1 = math.factorial(num1)
    fact2 = math.factorial(num2)
    result = fact1 / fact2
    print(f'{result:.2f}')


################################################
# RUN!
###########################################
# smallest_of_three_numbers()
# problem_2()
# characters_in_range()
# odd_and_even_sum()
# even_numbers()
# sorting()
# min_max_sum()
# palindrome_integers()

# x_pass = input()
# password_validator(x_pass)

# x_num = int(input())
# perfect_number(x_num)

# x_bar = int(input())
# loading_bar(x_bar)

# factorial_division()
characters_in_range_v2()
