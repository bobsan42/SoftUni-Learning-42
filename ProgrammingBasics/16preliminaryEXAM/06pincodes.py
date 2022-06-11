max_i1 = int(input())
max_i2 = int(input())
max_i3 = int(input())

list_i2 = [2, 3, 5, 7]
list_i13 = [2, 4, 6, 8]

for i1 in list_i13:
    if i1 > max_i1:
        break
    for i2 in list_i2:
        if i2 > max_i2:
            break
        for i3 in list_i13:
            if i3 > max_i3:
                break
            print(f'{i1} {i2} {i3}')
