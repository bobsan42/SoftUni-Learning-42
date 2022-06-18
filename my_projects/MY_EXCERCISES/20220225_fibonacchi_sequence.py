n_numbers = input("How many numbers do you want to calculate?")
n_numbers = int(n_numbers)
print_each = False
if input("Print each number? (y/n)") == 'y':
    print_each = True

columns_limit = 4
columns_counter = 0
previous_number = 0
current_number = 1

for i in range(0, n_numbers + 1):
    current_number += previous_number
    previous_number = current_number
    if print_each:
        print('{0:40d}'.format(current_number), end=' ')
        columns_counter += 1
        if columns_counter == columns_limit:
            columns_counter = 0
            print()
if not print_each:
    print('{0:,}'.format(current_number).replace(',', ' '))
