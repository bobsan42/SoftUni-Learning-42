start_code = input()
end_code = input()

for i0 in range(int(start_code[0]), int(end_code[0]) + 1):
    if i0 % 2 == 0:
        continue
    for i1 in range(int(start_code[1]), int(end_code[1]) + 1):
        if i1 % 2 == 0:
            continue
        for i2 in range(int(start_code[2]), int(end_code[2]) + 1):
            if i2 % 2 == 0:
                continue
            for i3 in range(int(start_code[3]), int(end_code[3]) + 1):
                if i3 % 2 == 0:
                    continue
                print(f'{i0}{i1}{i2}{i3}', end=' ')
