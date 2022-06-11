n_start = int(input())
n_end = int(input())

d1 = 0
d2 = 0
d3 = 0
d4 = 0

count_combinations = 0

for d1 in range(n_start, n_end + 1):
    for d2 in range(n_start, n_end + 1):
        for d3 in range(n_start, n_end + 1):
            if (d2 + d3) % 2 != 0:
                continue
            for d4 in range(n_start, n_end + 1):
                if d4 >= d1:
                    break
                if (d4 % 2) == (d1 % 2):
                    continue
                print(f'{d1}{d2}{d3}{d4}', end=' ')
                count_combinations += 1
