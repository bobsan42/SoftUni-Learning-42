fruit = input()
day = input()
qty = float(input())

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    a = 1
    b = 0
elif day == 'Saturday' or day == 'Sunday':
    a = 0
    b = 1
else:
    a = 0
    b = 0

price = 0
if fruit == 'banana':  # apple / orange / grapefruit / kiwi / pineapple / grapes;
    price = a * 2.50 + b * 2.70
elif fruit == 'apple':
    price = a * 1.20 + b * 1.25
elif fruit == 'orange':
    price = a * .85 + b * .90
elif fruit == 'grapefruit':
    price = a * 1.45 + b * 1.60
elif fruit == 'kiwi':
    price = a * 2.7 + b * 3
elif fruit == 'pineapple':
    price = a * 5.5 + b * 5.6
elif fruit == 'grapes':
    price = a * 3.85 + b * 4.2

if price == 0:
    print('error')
else:
    print(f'{(qty * price):.2f}')

