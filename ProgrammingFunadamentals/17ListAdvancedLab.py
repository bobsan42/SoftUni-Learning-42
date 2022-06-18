def no_vowels():
    text = input()
    vowels_list = ['a', 'e', 'o', 'u', 'i']
    result = [ch for ch in text if ch.lower() not in vowels_list]
    print(''.join(result))


def train():
    n_wagons = int(input())
    wagons = [0] * n_wagons
    command = input()

    while command != 'End':
        x = command.split()
        if x[0] == 'add':
            wagons[- 1] += int(x[1])
        elif x[0] == 'insert':
            wagons[int(x[1])] += int(x[2])
        elif x[0] == 'leave':
            wagons[int(x[1])] -= int(x[2])
        command = input()
    print(wagons)


def to_do_list():
    tasks_to_do = list()
    sorted_tasks = list()
    command = input()
    while command != 'End':
        x = command.split('-')
        priority = int(x[0])
        task = x[1]
        tasks_to_do.append((priority, task))
        sorted_tasks = [x[1] for x in sorted(tasks_to_do)]

        command = input()
    print(sorted_tasks)


def palindrome_strings():
    first_words = input()
    look_for = input()

    def is_palindrome(num: str):
        return num == num[::-1]

    # palindromes_found = [x for x in first_words.split() if x == x[::-1]]
    palindromes_found = [x for x in first_words.split() if is_palindrome(x)]

    print(palindromes_found)
    print(f'Found palindrome {palindromes_found.count(look_for)} times')


def sorting_names():
    names = input().split(', ')
    # sorted_list = sorted(sorted(names, reverse=True),key=len,reverse=True)
    # sorted_list = sorted(sorted(names), key=len, reverse=True)
    sorted_list = sorted(names, key=lambda item: (-len(item), item))
    print(sorted_list)


def even_numbers_indices():
    numbers = input().split(', ')
    even_indices = [idx for idx, num in enumerate(numbers) if int(num) % 2 == 0]
    print(even_indices)


def even_numbers_indices_v2():
    numbers = list(map(int, input().split(', ')))
    even_indices = [idx for idx, num in enumerate(numbers) if num % 2 == 0]
    print(even_indices)


def the_office():
    happiness_list = input().split()
    employees_count = len(happiness_list)
    improvement_factor = int(input())
    final_list = list(map(lambda x: int(x) * improvement_factor, happiness_list))
    average_happiness = sum(final_list) / employees_count
    happy_count = len(list(filter(lambda x: x >= average_happiness, final_list)))
    if happy_count < employees_count / 2:
        print(f'Score: {happy_count}/{employees_count}. Employees are not happy!')
    else:
        print(f'Score: {happy_count}/{employees_count}. Employees are happy!')


################################################
# RUN!
###########################################
# no_vowels()
# train()
# to_do_list()
# palindrome_strings()
# sorting_names()
# even_numbers_indices_v2()
the_office()
