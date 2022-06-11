n_male = int(input())
n_female = int(input())
n_tables_max = int(input())

tables_count = 0
for i in range(1, n_male + 1):
    if tables_count > n_tables_max:
        break
    for j in range(1, n_female + 1):
        tables_count += 1
        if tables_count > n_tables_max:
            break
        print(f'({i} <-> {j})', end=' ')
