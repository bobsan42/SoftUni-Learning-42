fruit = input()
set_size = input()
sets_ordered = int(input())
unit_price = 0
pieces_in_set = 0
if set_size == 'small':
    pieces_in_set = 2
    if fruit == 'Watermelon':
        unit_price = 56
    elif fruit == 'Mango':
        unit_price = 36.66
    elif fruit == 'Pineapple':
        unit_price = 42.10
    elif fruit == 'Raspberry':
        unit_price = 20
elif set_size == 'big':
    pieces_in_set = 5
    if fruit == 'Watermelon':
        unit_price = 28.70
    elif fruit == 'Mango':
        unit_price = 19.60
    elif fruit == 'Pineapple':
        unit_price = 24.80
    elif fruit == 'Raspberry':
        unit_price = 15.20

cost = unit_price * pieces_in_set * sets_ordered
if cost > 1000:
    cost *= .5
elif cost >= 400:
    cost *= .85

print(f'{cost:.2f} lv.')
