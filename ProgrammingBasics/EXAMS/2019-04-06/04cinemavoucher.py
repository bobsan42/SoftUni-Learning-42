voucher = int(input())
money_left = voucher
n_tickets = 0
n_others = 0
check = 8
while True:
    x = input()
    if x == 'End':
        break
    if len(x) > check:
        x_value = ord(x[0]) + ord(x[1])
        if x_value > money_left:
            break
        else:
            n_tickets += 1
    else:
        x_value = ord(x[0])
        if x_value > money_left:
            break
        else:
            n_others += 1
    money_left -= x_value
    if money_left == 0:
        break

print(n_tickets)
print(n_others)
