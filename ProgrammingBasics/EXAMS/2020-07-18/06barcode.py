a = input()
b = input()

for i1 in range(int(a[0]), int(b[0]) + 1):
    if i1 % 2 == 0:
        continue
    for i2 in range(int(a[1]), int(b[1]) + 1):
        if i2 % 2 == 0:
            continue
        for i3 in range(int(a[2]), int(b[2]) + 1):
            if i3 % 2 == 0:
                continue
            for i4 in range(int(a[3]), int(b[3]) + 1):
                if i4 % 2 == 0:
                    continue
                print(i1 * 1000 + i2 * 100 + i3 * 10 + i4, end=' ')


