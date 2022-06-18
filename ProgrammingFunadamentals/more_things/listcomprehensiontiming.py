import timeit

main_sequence = [1, 2, 3, 4, 5, 6]


def even_numbers_with_comprehension():
    # return [num for num in main_sequence if num % 2 ==0]
    return [num for num in main_sequence]


def even_numbers_with_loop():
    even_nums = []
    for num in main_sequence:
        # if num % 2 == 0:
        #     even_nums.append(num)
        even_nums.append(num)


print(timeit.timeit(even_numbers_with_comprehension))
print(timeit.timeit(even_numbers_with_loop))
