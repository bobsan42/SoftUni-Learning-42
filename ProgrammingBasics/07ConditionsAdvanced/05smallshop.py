prod = input()
city = input()
qty = float(input())

price = 0
if city == 'Sofia':
    if prod == 'coffee':
        price = .5
    elif prod == 'water':
        price = .8
    elif prod == 'beer':
        price = 1.2
    elif prod == 'sweets':
        price = 1.45
    elif prod == 'peanuts':
        price = 1.60
if city == 'Plovdiv':
    if prod == 'coffee':
        price = .4
    elif prod == 'water':
        price = .7
    elif prod == 'beer':
        price = 1.15
    elif prod == 'sweets':
        price = 1.30
    elif prod == 'peanuts':
        price = 1.50
if city == 'Varna':
    if prod == 'coffee':
        price = .45
    elif prod == 'water':
        price = .70
    elif prod == 'beer':
        price = 1.1
    elif prod == 'sweets':
        price = 1.35
    elif prod == 'peanuts':
        price = 1.55
cost = price * qty
print(cost)
