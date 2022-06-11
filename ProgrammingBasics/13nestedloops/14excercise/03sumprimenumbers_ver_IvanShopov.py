sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
command = input()

while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print('Number is negative.')
    else:
        # check if prime
        is_prime = True
        for i in range(2, int(current_number ** 0.5)+1):
            if current_number % i == 0:
                is_prime = False
                break
        # add to sums
        if is_prime:
            sum_of_prime_numbers += current_number
        else:
            sum_of_non_prime_numbers += current_number
    command = input()

print(f'Sum of all prime numbers is: {sum_of_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_of_non_prime_numbers}')
