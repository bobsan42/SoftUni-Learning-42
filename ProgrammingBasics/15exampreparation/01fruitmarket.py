price_strawberry = float(input())
qty_bananas = float(input())
qty_oranges = float(input())
qty_raspberies = float(input())
qty_strawberries = float(input())

price_raspberies = price_strawberry / 2
price_oranges = price_raspberies * .6
price_bananas = price_raspberies * .2

total_price = price_bananas * qty_bananas + \
              price_oranges * qty_oranges + \
              price_raspberies * qty_raspberies + \
              price_strawberry * qty_strawberries
print(f'{total_price:.2f}')
