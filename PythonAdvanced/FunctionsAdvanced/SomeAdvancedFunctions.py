# Packing arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    print(args)
    return result

# print(multiply([x for x in range(1,11)]))
print(multiply(*[x for x in range(1,11)])) #UNPACKING a list
print(multiply(1,2,3,4,5,6,7))

# Keyworded arguments
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{value}, {key}")

greet_me(Peter="Hello", George="Bye")
# Hello Peter
# Bye George

def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"

# TEST CODE
print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

