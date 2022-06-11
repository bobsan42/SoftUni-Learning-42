a_start = input()
a_end = input()
a_skip = input()
i_start = ord(a_start)
i_end = ord(a_end)
count_combinations = 0
a1 = ''
a2 = ''
a3 = ''
for i1 in range(i_start, i_end + 1):
    a1 = chr(i1)
    if a1 == a_skip:
        continue
    for i2 in range(i_start, i_end + 1):
        a2 = chr(i2)
        if a2 == a_skip:
            continue
        for i3 in range(i_start, i_end + 1):
            a3 = chr(i3)
            if a3 == a_skip:
                continue
            print(a1 + a2 + a3, end=' ')
            count_combinations += 1

print(count_combinations)
