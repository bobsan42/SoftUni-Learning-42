import operator


# problem 1
def abs_vals():
    nums = input()
    # opt1
    # result = list(map(float, nums.split()))
    # result = list(map(abs, result))
    # opt 2
    # result = list(map(lambda x: abs(float(x)), nums.split()))

    # opt3
    numbers = list(map(float, nums.split()))
    result = [abs(x) for x in numbers]

    print(result)


# problem 2
def grades():
    def check_grade(grade):
        grade = float(grade)
        if grade < 2:
            ...
        elif 2 <= grade <= 2.99:
            return 'Fail'
        elif 3 <= grade <= 3.49:
            return 'Poor'
        elif 3.50 <= grade <= 4.49:
            return 'Good'
        elif 4.50 <= grade <= 5.49:
            return 'Very Good'
        elif 5.50 <= grade <= 6.00:
            return 'Excellent'
        else:
            ...

    print(check_grade(input()))


# problem 3
def solve_calculations(operation: str, x: int, y: int):
    if operation == 'multiply':
        return x * y
    elif operation == 'divide':
        return int(x / y)
    elif operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y


def calculations():
    op = input()
    a = int(input())
    b = int(input())
    print(solve_calculations(op, a, b))


# problem 4
def repeat_string():
    given_string = input()
    counter = int(input())

    result = lambda a_str, n: a_str * n
    print(result(given_string, counter))


# problem 5
def calculate_order(product: str, qty: int):
    products = ['coffee', 'water', 'coke', 'snacks']
    prices = [1.50, 1.00, 1.40, 2.00]
    return qty * prices[products.index(product)]


def orders():
    product = input()
    qty = int(input())
    print(f'{calculate_order(product, qty):.2f}')


# problem 6
def rectangle_area():
    a = int(input())
    b = int(input())
    r_area = lambda x, y: x * y
    print(r_area(a, b))


# problem 7

def rounding():
    nums = input()
    numbers = list(map(float, nums.split()))
    result = list(map(round, numbers))
    print(result)


######################################################################
# RUN time
######################################################################
# abs_vals()
# grades()
# calculations()
# repeat_string()
# orders()
# rectangle_area()
# rounding()


# problem 2 - ADVANCED VERSION
# TODO: to study this piece of code and the relevant libraries
# import operator

def calculations_advanced(a, b, operation):
    operations_dict = {'multiply': operator.mul,
                       'divide': operator.truediv,
                       'add': operator.add,
                       'subtract': operator.sub}
    return int(operations_dict[operation](a, b))


aa = int(input())
bb = int(input())
operation_str = input()
print(calculations_advanced(aa, bb, operation_str))
