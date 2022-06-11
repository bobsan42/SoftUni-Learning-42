# import math


def isprime(x):  # T_O_D_O: Prime numbers function DONE
    is_prime = True
    i = int(x)
    if i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        is_prime = True
    elif i % 2 == 0:
        is_prime = False
    elif i <= 1: # negatives, 0 and 1 are NOT prime numbers
        is_prime = False
    else:
        # s = int(math.sqrt(i))
        s = int(i ** 0.5)
        for j in range(3, s + 1):
            if i % j == 0:
                is_prime = False
                break

    return is_prime


sum_primes = 0
sum_non_primes = 0
x = input()
while x != 'stop':
    j = int(x)
    if j < 0:
        print('Number is negative.')
    elif j == 0:
        pass
    else:
        if isprime(j):
            sum_primes += j
            # print(f"{j} is prime")
        else:
            sum_non_primes += j
            # print(f"{j} is NOT prime")
    x = input()

print(f'Sum of all prime numbers is: {sum_primes}')
print(f'Sum of all non prime numbers is: {sum_non_primes}')
