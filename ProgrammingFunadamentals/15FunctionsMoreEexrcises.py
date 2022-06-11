import math


def data_types():
    data_type = input()
    data_text = input()
    result = None
    if data_type == 'int':
        result = int(data_text) * 2
    elif data_type == 'real':
        result = f'{(float(data_text) * 1.5):.2f}'
    elif data_type == 'string':
        result = '$' + data_text + '$'
    print(result)


def closer_point():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    distance1 = (x1 ** 2 + y1 ** 2) ** .5
    distance2 = (x2 ** 2 + y2 ** 2) ** .5

    if distance2 < distance1:
        print(f'({math.floor(x2)}, {math.floor(y2)})')
    else:
        print(f'({math.floor(x1)}, {math.floor(y1)})')


def longer_line():
    def get_line():
        line = [0]  # line[length, point1[distance_to_0,x,y], point2[distance_to_0,x,y]]
        for _ in range(2):
            x = float(input())
            y = float(input())
            distance = (x ** 2 + y ** 2) ** .5
            line.append([distance, x, y])
        delta_x = abs(line[1][1] - line[2][1])
        delta_y = abs(line[1][2] - line[2][2])
        line_length = (delta_x ** 2 + delta_y ** 2) ** .5
        line[0] = line_length
        if line[1][0] > line[2][0]:  # compare the distances to the 0
            line[1], line[2] = line[2], line[1]
        return line

    def print_line(line_data):
        a = line_data.copy()
        for point in a[1:]:
            b = list(map(math.floor, point[1:]))
            c = b[1:]
            c = list(map(str, b))
            result = ', '.join(c)
            print(f'({result})', end='')

    first_line = get_line()
    second_line = get_line()
    if first_line[0] < second_line[0]:
        print_line(second_line)
    else:
        print_line(first_line)


def tribonacci_sequence():
    sequence_length = int(input())
    sequence = [1]
    for _ in range(sequence_length - 1):
        x = sum(sequence[-3:])
        sequence.append(x)
    print(*sequence)


def multiplication_sign():
    nums = []
    multi_sign = 'positive'
    for _ in range(3):
        nums.append(int(input()))
    if nums.count(0) > 0:
        multi_sign = 'zero'
    else:
        # negatives = []
        negatives = list(filter(lambda x: x < 0, nums))
        if len(negatives) % 2 != 0:
            multi_sign = 'negative'
    print(multi_sign)


# # # # # # # # # # # # # # # # # # # # # # # # # #
# RUN TIME
# # # # # # # # # # # # # # # # # # # # # # # # # #

# data_types()
# closer_point()
# longer_line()

# tribonacci_sequence()

multiplication_sign()
