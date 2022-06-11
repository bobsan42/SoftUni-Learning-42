budget = float(input())
fuel_needed = float(input())
day_of_the_week = input()

fuel_cost = 2.1 * fuel_needed
cost_guide = 100
total_cost = fuel_cost + cost_guide

if day_of_the_week == "Saturday":
    total_cost *= 0.9
elif day_of_the_week == "Sunday":
    total_cost *= .8

diff = abs(total_cost - budget)

if total_cost > budget:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')
else:
    print(f'Safari time! Money left: {diff:.2f} lv. ')
