from math import ceil

price_beer = 1.20
chips_pack_price_percentage = .45  # 45% of the price of all beers, round up INT

fan_name = input()
budget = float(input())
n_beers = int(input())
n_chips_packs = int(input())

cost_beers = price_beer * n_beers
price_chips = (chips_pack_price_percentage * cost_beers)
cost_chips = ceil(price_chips * n_chips_packs)
cost = cost_beers + cost_chips
diff = abs(cost - budget)
if cost > budget:
    print(f"{fan_name} needs {diff:.2f} more leva!")
else:
    print(f"{fan_name} bought a snack and has {diff:.2f} leva left.")
