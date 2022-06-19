def which_are_in():
    first_string = input().split(', ')
    second_string = input().split(', ')
    found_list = []
    for x in first_string:
        for y in second_string:
            if x in y:
                found_list.append(x)
                break
    print(found_list)


def next_version():
    version_string = input().split('.')
    version = list(map(int, version_string))[::-1]
    for i in range(len(version)):
        version[i] += 1
        if version[i] > 9:
            version[i] = 0
        else:
            break

    version.reverse()
    version_string = list(map(str, version))
    print('.'.join(version_string))


def word_filter():
    word_list = input().split()
    result = [x for x in word_list if len(x) % 2 == 0]
    for x in result:
        print(x)


def numbers_classificator():
    numbers_list = input().split(', ')
    res = [x for x in numbers_list if int(x) >= 0]
    print(f"Positive: {', '.join(res)}")
    res = [x for x in numbers_list if int(x) < 0]
    print(f"Negative: {', '.join(res)}")
    res = [x for x in numbers_list if int(x) % 2 == 0]
    print(f"Even: {', '.join(res)}")
    res = [x for x in numbers_list if int(x) % 2 != 0]
    print(f"Odd: {', '.join(res)}")


def office_chairs():
    n_rooms = int(input())
    free_chairs = 0
    enough_chairs = True
    for i in range(n_rooms):
        x = input().split()
        chairs = len(x[0])
        visitors = int(x[1])
        if chairs < visitors:
            print(f'{visitors - chairs} more chairs needed in room {i + 1}')
            enough_chairs = False
        else:
            free_chairs += chairs - visitors

    if enough_chairs:
        print(f'Game On, {free_chairs} free chairs left')


def electron_distribution():
    electrons = int(input())
    shells = []
    position = 0
    while electrons > 0:
        position += 1
        max_electrons = min(2 * (position ** 2), electrons)
        shells.append(max_electrons)
        electrons -= max_electrons

    print(shells)


def group_of_tens():
    numbers = input().split(', ')
    nums = list(map(int, numbers))
    boundary = 0
    while len(nums) > 0:
        boundary += 10
        grouped = []
        for x in nums:
            if x <= boundary:
                grouped.append(x)
        for x in grouped:
            nums.remove(x)
        print(f'Group of {boundary}\'s: {grouped}')


def decipher_this():
    message = input().split()

    def first_letter(word: str):
        first_letter_code = ''
        other_letters = ''
        for char in word:
            if ord('0') <= ord(char) <= ord('9'):
                first_letter_code += char
            else:
                other_letters += char
        final_word = [chr(int(first_letter_code))]
        final_word += list(other_letters)
        final_word[1], final_word[-1] = final_word[-1], final_word[1]
        return ''.join(final_word)

    deciphered_message = ''
    for word in message:
        deciphered_message += first_letter(word) + ' '
    print(deciphered_message)


def anonymous_threat():
    def merger(list_to_merge, start_idx: int, end_idx: int):
        # Merge the elements of the given list from start index to end index, inclusive
        # returns the new shorter list
        ###############################################
        # Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex.
        # In other words, you should concatenate them.
        # Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
        # If any of the given indexes is out of the array,
        # you must take only the range that is inside the array and merge it.

        merge_result = []
        merged_elements = ''
        for idx, x in enumerate(list_to_merge):
            if idx < start_idx or idx > end_idx:
                merge_result.append(x)
            else:
                merged_elements += x
                if idx == end_idx:
                    merge_result.append(merged_elements)
        return merge_result

    def divider(list_to_divide, list_index: int, partitions: int):
        ...

    input_line = input()
    strings_list = input_line.split()
    command = input()
    # •	merge {startIndex} {endIndex}
    # •	divide {index} {partitions}
    result = strings_list.copy()

    while command != '3:1':
        cmd = command.split()
        if cmd[0] == 'merge':
            result = merger(result, int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'divide':
            ...
        command = input()
    print(' '.join(result))


# Driver code
if __name__ == '__main__':
    # function call
    # which_are_in()
    # next_version()
    # word_filter()
    # numbers_classificator()
    # office_chairs()
    # electron_distribution()
    # group_of_tens()
    # print(timeit.timeit(decipher_this))
    # decipher_this()
    anonymous_threat()
