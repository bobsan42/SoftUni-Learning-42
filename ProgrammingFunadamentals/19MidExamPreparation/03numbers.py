# https://judge.softuni.org/Contests/Practice/Index/2474#2

def numbers_function():
    init_sequence = input().split()
    numbers_list = list(map(int, init_sequence))
    average_num = sum(numbers_list) / len(numbers_list)
    larger_numbers = [x for x in numbers_list if x > average_num]
    larger_numbers.sort(reverse=True)
    result = larger_numbers[:5]
    result = list(map(str, result))
    if len(result) == 0:
        print('No')
    else:
        print(' '.join(result))


numbers_function()
