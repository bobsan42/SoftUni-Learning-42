fruit = input()
day = input()
qty = float(input())

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    y = 'Working day'
elif day == 'Saturday' or day == 'Sunday':
    y = 'Weekend'
else:
    y = 'error'

price = 0
if y != 'error':
    if fruit == 'banana':  # apple / orange / grapefruit / kiwi / pineapple / grapes;
        price = 2.70 if y == 'Weekend' else 2.50
    elif fruit == 'apple':
        price = 1.25 if y == 'Weekend' else 1.20
    elif fruit == 'orange':
        price = .90 if y == 'Weekend' else .85
    elif fruit == 'grapefruit':
        price = 1.6 if y == 'Weekend' else 1.45
    elif fruit == 'kiwi':
        price = 3 if y == 'Weekend' else 2.70
    elif fruit == 'pineapple':
        price = 5.60 if y == 'Weekend' else 5.50
    elif fruit == 'grapes':
        price = 4.20 if y == 'Weekend' else 3.85

if price == 0:
    print('error')
else:
    print(f'{(qty * price):.2f}')
