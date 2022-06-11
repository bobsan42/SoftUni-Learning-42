max_i1 = int(input())
max_i2 = int(input())
max_i3 = int(input())

for i1 in range(1, max_i1 + 1):
    if i1 % 2 != 0:
        continue
    for i2 in range(2, max_i2 + 1):
        is_prime = True
        for div in range(2, i2):
            if i2 % div == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        for i3 in range(1, max_i3 + 1):
            if i3 % 2 != 0:
                continue
            print(f'{i1} {i2} {i3}')
