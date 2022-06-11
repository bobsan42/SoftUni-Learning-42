def test1(x: int):
    if x < 10:
        test1(x + 1)
    else:
        exit
    print(x)


test1(9)


def test2(first_name='George', last_name='Brown'):
    print(first_name, last_name)


test2('Peter')
test2(last_name='Smith', first_name='John')


def test3():
    x = lambda a: a + 10
    print(x(5))
    x = lambda a, b: a * b
    print(x(4, 3))
    x = lambda first, last: f'I am {first} {last}.'
    print(x('John', 'Smith'))


test3()


def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def test_filter():
    numbers = [1, 2, 3, 5, 8, 9, 15, 16, 18, 22, 35, 48]
    result = list(filter(lambda x: x % 2 != 0, numbers))  # odds only
    print(result)
    result = list(filter(lambda x: x % 2 == 0, numbers))  # evens only
    print(result)
    result = list(filter(check_even, numbers))  # evens only
    print(result)


test_filter()


def test_map():
    numbers = [2, 4, 6, 8, 10]

    def square_nums(num):
        return num * num

    squares_list = list(map(square_nums, numbers))
    print(squares_list)


test_map()


def test_doc_string():
    '''This function is just a test to show the doc string
This function is just a test to show the doc string - line 2'''
    ...


print(test_doc_string.__doc__)
