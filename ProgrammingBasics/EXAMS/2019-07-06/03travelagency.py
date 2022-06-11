city = input()  # "Bansko",  "Borovets", "Varna" , "Burgas"
package = input()  # "noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast"
has_vip = input()
has_vip = (has_vip == "yes")
vip_discount = 0
price = 0
n_days = int(input())
is_valid = True

if city == 'Bansko' or city == 'Borovets':
    if package == 'noEquipment':
        price = 80
        vip_discount = 5 / 100
    elif package == 'withEquipment':
        price = 100
        vip_discount = 10 / 100
    else:
        is_valid = False
elif city == 'Varna' or city == 'Burgas':
    if package == 'withBreakfast':
        price = 130
        vip_discount = 12 / 100
    elif package == 'noBreakfast':
        price = 100
        vip_discount = 7 / 100
    else:
        is_valid = False
else:
    is_valid = False

if not is_valid:
    print("Invalid input!")
elif n_days < 1:
    print("Days must be positive number!")
else:
    if n_days > 7:
        n_days -= 1
    cost = price * n_days
    if has_vip:
        cost *= (1 - vip_discount)
    print(f"The price is {cost:.2f}lv! Have a nice time!")
