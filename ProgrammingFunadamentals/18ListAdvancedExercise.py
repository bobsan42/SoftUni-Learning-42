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
        # Every time you receive the merge command,
        # you must merge all elements from the startIndex to the endIndex.
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
                if idx == end_idx or idx == len(list_to_merge) - 1:
                    merge_result.append(merged_elements)
        return merge_result

    def divider(list_to_divide, list_index: int, partitions: int):
        # Divides an element from the list to the given number of partitions
        # #####################################################
        # Every time you receive the divide command,
        # you must divide the element at the given index into several small substrings with equal length.
        # The count of the substrings should be equal to the given partitions.
        # Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
        # If the string cannot be exactly divided into the given partitions,
        # make all partitions except the last with equal lengths and make the last one - the longest.
        # Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
        divide_result = []
        if partitions == 1:
            divide_result = list_to_divide.copy()
        else:
            for idx, x in enumerate(list_to_divide):
                if idx != list_index:
                    divide_result.append(x)
                else:
                    length = len(x) // partitions
                    i = 0
                    for _ in range(partitions - 1):
                        i = _
                        divide_result.append(x[0 + length * i:length + length * i])
                    divide_result.append(x[0 + length * (i + 1):])
        return divide_result

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
            result = divider(result, int(cmd[1]), int(cmd[2]))
        command = input()
    print(' '.join(result))


def pokemon_dont_go():
    seq = input().split()
    nums = list(map(int, seq))
    sum_of_removed_elements = 0
    while len(nums) > 0:
        idx = int(input())
        if idx < 0:
            x = nums[0]
            nums[0] = nums[-1]
        elif idx > len(nums) - 1:
            x = nums[-1]
            nums[-1] = nums[0]
        else:
            x = nums.pop(idx)
        sum_of_removed_elements += x
        for ind, num in enumerate(nums):
            if num <= x:
                nums[ind] += x
            else:
                nums[ind] -= x
    print(sum_of_removed_elements)


def softuni_course_planning(): # TODO: JUDGE check 66/100
    init_schedule = input().split(', ')
    final_schedule = init_schedule.copy()
    command = input()
    suffix = '-Exercise'
    while command != 'course start':
        cmd = command.split(':')
        lesson_title = cmd[1]
        if cmd[0] == 'Add':
            if lesson_title not in final_schedule:
                final_schedule.append(lesson_title)
        elif cmd[0] == 'Insert':
            idx = int(cmd[2])
            if lesson_title not in final_schedule:
                final_schedule.insert(idx, lesson_title)
        elif cmd[0] == 'Remove':
            for _ in range(2):
                if lesson_title in final_schedule:
                    final_schedule.remove(lesson_title)
                lesson_title += suffix
        elif cmd[0] == 'Swap':
            idx = [None] * 3
            if cmd[1] in final_schedule and cmd[2] in final_schedule:
                idx[1] = final_schedule.index(cmd[1])
                idx[2] = final_schedule.index(cmd[2])
                final_schedule[idx[1]], final_schedule[idx[2]] = final_schedule[idx[2]], final_schedule[idx[1]]
                # cmd[2],cmd[1] = cmd[1],cmd[2]
                for i in range(1, 3):
                    exercise_title = cmd[i] + suffix
                    if exercise_title in final_schedule:
                        final_schedule.remove(exercise_title)
                        idx[i] = final_schedule.index(cmd[i])
                        final_schedule.insert(idx[i] + 1, exercise_title)
        elif cmd[0] == 'Exercise':
            exercise_title = lesson_title + suffix
            if lesson_title not in final_schedule:
                final_schedule.append(lesson_title)
            if exercise_title in final_schedule:
                final_schedule.remove(exercise_title)
            final_schedule.insert(final_schedule.index(lesson_title), exercise_title)
        command = input()
    idx = 0
    for lesson in final_schedule:
        idx += 1
        print(f'{idx}.{lesson}')


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
    # anonymous_threat()
    # pokemon_dont_go()
    softuni_course_planning()
