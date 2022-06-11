max1 = int(input())
max2 = int(input())
max3 = int(input())

list_d2 = [2, 3, 5, 7]

for d1 in range(1, 10):
    if d1 % 2 == 1:
        continue
    if d1 > max1:
        break
    for d2 in list_d2:
        if d2 > max2:
            break
        for d3 in range(1, 10):
            if d3 % 2 == 1:
                continue
            if d3 > max3:
                break
            print(f'{d1} {d2} {d3}')
