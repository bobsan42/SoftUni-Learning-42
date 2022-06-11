n = int(input())
low = 1111
high = 9999

for i in range(low, high + 1):
    is_special = True
    # for idx, dig in enumerate(str(i)):
    if "0" in str(i):  # instead of if dig == '0':
        continue
    for dig in str(i):
        # if dig == '0':
        #     is_special = False
        #     break
        # elif n % int(dig) != 0:
        if n % int(dig) != 0:
            is_special = False
            break
    if is_special:
        print(i, end=' ')
