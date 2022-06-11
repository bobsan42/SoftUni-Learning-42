fuel_type = input()
fuel_qty = float(input())
discount_card = input()

if discount_card == 'Yes':
    disc = 1
else:
    disc = 0

fuel_price = 0
if fuel_type == "Gasoline":  # benzin
    fuel_price = 2.22 - .18 * disc
elif fuel_type == "Diesel":
    fuel_price = 2.33 - .12 * disc
elif fuel_type == "Gas":
    fuel_price = .93 - .08 * disc

total_cost = fuel_qty * fuel_price
if fuel_qty > 25:
    total_cost *= .9
elif fuel_qty >= 20:
    total_cost *= .92

print(f'{total_cost:.2f} lv.')
