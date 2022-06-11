ones = int(input())
twos = int(input())
fives = int(input())
target_sum = int(input())

ni = min(ones, int(target_sum // 1))
for i in range(0, ni + 1):
    nj = min(twos, int((target_sum - i * 1) // 2))
    for j in range(0, nj + 1):
        nk = min(fives, int((target_sum - i * 1 - j * 2) // 5))
        for k in range(0, nk + 1):
            if target_sum == i * 1 + j * 2 + k * 5:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {target_sum} lv.')
