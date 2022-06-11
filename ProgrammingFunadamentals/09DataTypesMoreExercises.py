def exchange_integers():
    a = int(input())
    b = int(input())
    print('Before:')
    print(f'a = {a}')
    print(f'b = {b}')
    c = a
    a = b
    b = c
    print('After:')
    print(f'a = {a}')
    print(f'b = {b}')


def prime_number_checker():
    x = int(input())
    is_prime = True
    i = x
    if i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        is_prime = True
    elif i % 2 == 0:
        is_prime = False
    elif i <= 1:  # negatives, 0 and 1 are NOT prime numbers
        is_prime = False
    else:
        s = int(i ** 0.5)
        for j in range(3, s + 1):
            if i % j == 0:
                is_prime = False
                break

    print(is_prime)


def decrypting_messages():
    key = int(input())
    n_lines = int(input())
    message = ''
    for _ in range(n_lines):
        letter = input()
        message += chr(ord(letter) + key)
    print(message)


def balanced_brackets():
    n = int(input())
    is_opened = False
    is_balanced = True
    for _ in range(n):
        char = input()
        if not is_balanced:
            continue
        if char == '(':
            if is_opened:
                is_balanced = False
                continue
            else:
                is_opened = True
        elif char == ')':
            if is_opened:
                is_opened = False
            else:
                is_balanced = False
                continue
        else:
            ...

    if is_balanced:
        print('BALANCED')
    else:
        print('UNBALANCED')


################################################
# RUN!
###########################################
balanced_brackets()