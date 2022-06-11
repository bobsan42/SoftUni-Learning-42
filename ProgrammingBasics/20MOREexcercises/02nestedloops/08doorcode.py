hundreds_max = int(input())
tens_max = int(input())
ones_max = int(input())

tens_list = [2, 3, 5, 7]

for hundreds in range(2, hundreds_max + 1, 2):
    for tens in tens_list:
        if tens > tens_max:
            break
        for ones in range(2, ones_max + 1, 2):
            print(f'{hundreds} {tens} {ones}')
