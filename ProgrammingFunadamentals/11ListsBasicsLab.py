def test_using_arrays():
    import array as arr
    test = arr.array("i", [10, 20, 30, 30, 40, 50])
    print(test[0])
    print(type(test))
    print(type(test[0]))


def test_using_arrays_2():
    import numpy as np
    test = np.array([10, 20, 30, 30, 40, 50])
    print(test[0])
    print(type(test))
    print(type(test[0]))


def strange_zoo():
    tail = input()
    body = input()
    head = input()

    # head, body, tail = tail, body, head
    animal = [head, body, tail]
    print(animal)


def courses():
    n = int(input())
    courses_list = []
    for _ in range(n):
        x = input()
        courses_list.append(x)
    print(courses_list)


def statistics_list():
    n = int(input())
    positives_list = []
    negatives_list = []
    # sum_of_negatives = 0
    for _ in range(n):
        x = int(input())
        if x < 0:
            negatives_list += [x]
            # sum_of_negatives += x
        else:
            positives_list.append(x)

    print(positives_list)
    print(negatives_list)
    print(f'Count of positives: {len(positives_list)}')
    print(f'Sum of negatives: {sum(negatives_list)}')


def search():
    n = int(input())
    word = input()
    strings_list = []
    for _ in range(n):
        x = input()
        strings_list.append(x)
    print(strings_list)
    for i in range(len(strings_list) - 1, -1, -1):
        if word not in strings_list[i]:
            strings_list.pop(i)
    print(strings_list)


def numbers_filter():
    n = int(input())
    nums_list = []
    for _ in range(n):
        x = int(input())
        nums_list.append(x)
    command = input()
    filtered_numbers = []
    for num in nums_list:
        if command == 'even':
            if num % 2 == 0:
                filtered_numbers.append(num)
        elif command == 'odd':
            if num % 2 == 1:
                filtered_numbers.append(num)
        elif command == 'negative':
            if num < 0:
                filtered_numbers.append(num)
        elif command == 'positive':
            if num >= 0:
                filtered_numbers.append(num)
    print(filtered_numbers)


def numbers_filter_v2():
    n = int(input())
    nums_list = []
    for _ in range(n):
        x = int(input())
        nums_list.append(x)
    command = input()
    filtered_numbers = []
    for num in nums_list:
        is_match = (
                (command == 'even' and num % 2 == 0) or
                (command == 'odd' and num % 2 == 1) or
                (command == 'negative' and num < 0) or
                (command == 'positive' and num >= 0))
        if is_match:
            filtered_numbers.append(num)
    print(filtered_numbers)


######################################################################
# RUN time
######################################################################
# search()
# numbers_filter()
numbers_filter_v2()