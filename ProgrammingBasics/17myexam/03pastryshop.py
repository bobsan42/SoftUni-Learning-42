prices_list = [  # before or on 15th december / after 15th december
    [24, 28.70],  # Cake
    [6.66, 9.80],  # Souffle
    [12.60, 16.98]  # Baklava
]  # prices are lv./pc

sweet_type = input()
n_sweets = int(input())
day_number = int(input())  # day in december
sweet_price = 0

if sweet_type == "Cake":
    prices = prices_list[0]
elif sweet_type == "Souffle":
    prices = prices_list[1]
elif sweet_type == "Baklava":
    prices = prices_list[2]

if day_number > 15:
    sweet_price = prices[1]
else:
    sweet_price = prices[0]

total_cost = sweet_price * n_sweets
if day_number < 23:
    if total_cost > 200:
        total_cost *= .75
    elif total_cost >= 100:
        total_cost *= .85
if day_number < 16:
    total_cost *= .9
print(f'{total_cost:.2f}')
