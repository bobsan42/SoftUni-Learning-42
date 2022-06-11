budget = float(input())
destination = input()
season = input()
n_days = int(input())
discount_percent = 0
price_per_day = 0

if destination == "Dubai":
    discount_percent = 30
    if season == "Winter":
        price_per_day = 45000
    elif season == 'Summer':
        price_per_day = 40000
elif destination == "Sofia":
    discount_percent = -25
    if season == "Winter":
        price_per_day = 17000
    elif season == 'Summer':
        price_per_day = 12500
elif destination == "London":
    discount_percent = 0
    if season == "Winter":
        price_per_day = 24000
    elif season == 'Summer':
        price_per_day = 20250

total_cost = n_days * price_per_day
total_cost *= (100 - discount_percent) / 100
diff = abs(total_cost - budget)

if total_cost > budget:
    print(f'The director needs {diff:.2f} leva more!')
else:
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')
