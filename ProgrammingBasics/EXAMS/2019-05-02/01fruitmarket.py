price_strawberry = float(input())
qty_bananas = float(input())
qty_oranges = float(input())
qty_raspberry = float(input())
qty_strawberry = float(input())

price_raspberry = price_strawberry / 2
price_oranges = .6 * price_raspberry
price_bananas = .2 * price_raspberry

cost = qty_bananas * price_bananas + \
       qty_oranges * price_oranges + \
       qty_raspberry * price_raspberry + \
       qty_strawberry * price_strawberry

print('{:.2f}'.format(cost))
