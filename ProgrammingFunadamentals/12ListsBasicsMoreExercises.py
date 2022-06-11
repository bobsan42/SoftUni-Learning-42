def zeros_to_back():
    numbers_list = input().split(', ')
    for idx, num in enumerate(numbers_list):
        numbers_list[idx] = int(num)
    for idx in range(len(numbers_list) - 1, -1, -1):
        if numbers_list[idx] == 0:
            numbers_list.pop(idx)
            numbers_list.append(0)
    print(numbers_list)


def messaging():
    sequence = input().split()
    some_string = list(input())
    indices = []
    message = ''
    for x in sequence:
        idx = 0
        for y in list(x):
            idx += int(y)
        indices.append(idx)
    for idx in indices:
        while idx > len(some_string) - 1:
            idx -= len(some_string)
        message += some_string[idx]
        some_string.pop(idx)
    print(message)


def car_race():
    sequence_of_numbers = input().split()
    # winner = ''
    time_left = 0
    time_right = 0
    loops = int(len(sequence_of_numbers) / 2)
    for time in sequence_of_numbers[:loops]:
        if time == '0':
            time_left *= .8
        else:
            time_left += int(time)
    for time in sequence_of_numbers[:loops:-1]:
        if time == '0':
            time_right *= .8
        else:
            time_right += int(time)

    if time_left < time_right:
        winner = 'left'
    else:
        winner = 'right'
    print(f'The winner is {winner} with total time: {min(time_left, time_right):.1f}')


def josephus_permutation():
    initial_sequence = input().split()
    k = int(input())  # skip count
    execution_sequence = []
    idx = 0
    j = 1
    # print(initial_sequence)
    while initial_sequence:
        if j == k:
            j = 1
            execution_sequence.append((initial_sequence.pop(idx)))
        else:
            j += 1
            idx += 1
        if idx >= len(initial_sequence):
            idx = 0

    # print(execution_sequence)
    result = ','.join(execution_sequence)
    print(f'[{result}]')


def tic_tac_toe():
    line1 = input().split()
    line2 = input().split()
    line3 = input().split()
    winner = None

    winning_lines = [line1, line2, line3]
    for i in range(3):
        winning_lines.append([line1[i], line2[i], line3[i]])
    winning_lines.append([line1[0], line2[1], line3[2]])
    winning_lines.append([line1[2], line2[1], line3[0]])

    for i in ['1', '2']:
        if winner is not None:
            break
        for line in winning_lines:
            if line.count(i) == 3:
                if i == '1':
                    winner = 'First'
                elif i == '2':
                    winner = 'Second'
                break

    if winner is None:
        print('Draw!')
    else:
        print(f'{winner} player won')


def list_manipulator():
    global remainder
    initial_list = input().split()
    command = input()
    while command != 'end':
        cmd = command.split()
        if cmd[0] == 'exchange':
            idx = int(cmd[1])
            if (idx > len(initial_list) - 1) or idx < 0:
                print('Invalid index')
            else:
                initial_list = initial_list[idx + 1:] + initial_list[:idx + 1]
        elif cmd[0] == 'max' or cmd[0] == 'min':
            if cmd[1] == 'odd':
                remainder = 1
            elif cmd[1] == 'even':
                remainder = 0
            max_n = None
            max_idx = None
            for i in range(len(initial_list)):
                x = int(initial_list[i])
                if x % 2 != remainder:
                    continue
                if (max_n is None) or \
                        (cmd[0] == 'max' and (max_n <= x)) or \
                        (cmd[0] == 'min' and (max_n >= x)):
                    max_n = x
                    max_idx = i
            if max_idx is None:
                print('No matches')
            else:
                print(max_idx)
        elif cmd[0] == 'first' or cmd[0] == 'last':
            result = []
            if cmd[2] == 'odd':
                remainder = 1
            elif cmd[2] == 'even':
                remainder = 0
            counter = int(cmd[1])
            if counter > len(initial_list):
                print('Invalid count')
            else:
                if cmd[0] == 'first':
                    idx_list = list(range(len(initial_list)))
                elif cmd[0] == 'last':
                    idx_list = list(range(len(initial_list) - 1, -1, -1))
                for i in idx_list:
                    x = int(initial_list[i])
                    if x % 2 != remainder:
                        continue
                    result.append(x)
                    if len(result) == counter:
                        break
                if cmd[0] == 'last' and len(result) > 0:
                    result.reverse()
                print(result)

        command = input()
    # for i, v in enumerate(initial_list):
    #     initial_list[i] = int(v)
    print([int(x) for x in initial_list])


######################################################################
# RUN time
######################################################################
# zeros_to_back()
# messaging()
# car_race()
# josephus_permutation()
# tic_tac_toe()
list_manipulator()
