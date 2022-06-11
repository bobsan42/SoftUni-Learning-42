budget = int(input())
season = input()
n_fishermen = int(input())

is_disc = (n_fishermen % 2 == 0)
boat_rent = 0
if season == 'Spring':
    boat_rent = 3000
elif season == 'Summer':
    boat_rent = 4200
elif season == 'Autumn':
    boat_rent = 4200
    is_disc = False
elif season == 'Winter':
    boat_rent = 2600

discount1 = 0
if n_fishermen >= 12:
    discount1 = 25
elif n_fishermen >= 7:
    discount1 = 15
elif n_fishermen > 0:
    discount1 = 10

discount2 = 5 if is_disc else 0

cost = boat_rent * (1 - discount1 / 100) * (1 - discount2 / 100)
diff = abs(budget - cost)

if cost > budget:
    print(f'Not enough money! You need {diff:.2f} leva.')
else:
    print(f'Yes! You have {diff:.2f} leva left.')
