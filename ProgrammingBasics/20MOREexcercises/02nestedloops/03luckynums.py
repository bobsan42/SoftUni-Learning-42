n = int(input())

d1 = 0
d2 = 0
d3 = 0
d4 = 0
count_combinations = 0

for d1 in range(1, 10):
    if d1 >= n:
        break
    for d2 in range(1, 10):
        sum_left = d1 + d2
        if sum_left > n:
            break
        if n % sum_left != 0:
            continue
        for d3 in range(1, 10):
            if d3 >= sum_left:
                break
            d4 = sum_left - d3
            if d4>9:
                continue
            print(f'{d1}{d2}{d3}{d4}',end=' ')
            count_combinations += 1
