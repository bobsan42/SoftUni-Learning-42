def find_the_largest():
    original_number = input()
    index_list = []
    largest_number: str = ''
    while len(index_list) < len(original_number):
        max_digit = -1
        max_index = -1
        for idx, dig in enumerate(original_number):
            if idx not in index_list:
                if max_digit < int(dig):
                    max_digit = int(dig)
                    max_index = idx

        index_list.append(max_index)

    for idx in index_list:
        largest_number += original_number[idx]

    print(largest_number)


def find_the_capitals():
    original_string = input()
    list_capitals_indexes = []
    for idx, letter in enumerate(original_string):
        if 64 < ord(letter) < 91:
            list_capitals_indexes.append(idx)
    # if len(list_capitals_indexes) > 0:
    #     print(list_capitals_indexes)
    print(list_capitals_indexes)
    list_capitals_indexes.reverse()


def wolf_in_sheep_clothing():
    animals_order = input()
    # animals_order += ', me'
    animals_list = animals_order.split(', ')
    idx_wolf = animals_list.index('wolf')
    if idx_wolf + 1 == len(animals_list):
        print('Please go away and stop eating my sheep')
        exit()
    else:
        print(f'Oi! Sheep number {len(animals_list) - idx_wolf - 1}! You are about to be eaten by a wolf!')


def sum_of_a_beach():
    given_string = input()
    lower_string = given_string.lower()
    words_list = ['sand', 'water', 'fish', 'sun']
    total_sum = 0
    for element in words_list:
        total_sum += lower_string.count(element)
    print(total_sum)


################################################
# RUN!
###########################################
sum_of_a_beach()
