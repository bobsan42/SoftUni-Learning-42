def factorial(number):
    if not isinstance(number, int) or number < 0:
        return f"Sorry. 'number' is incorrect."

    def inner_factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

    return inner_factorial(number)


# Function, returning a Nested function:
# Returns a function depending on the operator
def calculator(operator):
    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    if operator == "+":
        return addition
    elif operator == "-":
        return subtraction


operation = calculator("+")
result = operation(2, 3)
print(result)

# Lexical Closures
# The inner function can capture and carry some of the parent function's state
def outside_function(number):
    def inside_function():
        return number
    return inside_function

print(outside_function(10)()) # 10

def greeting(name):
    hello = "Hello, "
    def say_hi():
        return hello + name
    return say_hi

print(greeting("Peter")())
# Hello, Peter
