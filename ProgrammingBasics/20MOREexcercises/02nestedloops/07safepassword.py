# password template: ABxyBA
a = int(input())
b = int(input())
max_password_count = int(input())
i = 0
minA = 35
maxA = 55
codeA = minA - 1
minB = 64
maxB = 96
codeB = minB - 1
password_count = 0

for x in range(1, a + 1):
    if password_count >= max_password_count:
        break
    for y in range(1, b + 1):
        if codeA >= maxA:
            codeA = minA
        else:
            codeA += 1
        A = chr(codeA)
        if codeB >= maxB:
            codeB = minB
        else:
            codeB += 1
        B = chr(codeB)
        print(f'{A}{B}{x}{y}{B}{A}', end='|')
        password_count += 1
        if password_count >= max_password_count:
            break
