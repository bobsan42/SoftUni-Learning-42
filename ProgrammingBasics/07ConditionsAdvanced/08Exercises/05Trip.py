budget = float(input())
season = input()

destination = 'Europe'
sleep_type = 'Hotel'
budget_part = 0.9

if 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        sleep_type = 'Camp'
        budget_part = .4
    elif season == 'winter':
        budget_part = .8
elif budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        sleep_type = 'Camp'
        budget_part = 0.3
    elif season == 'winter':
        budget_part = .7
cost = budget * budget_part
out_line_1 = f'Somewhere in {destination}'
out_line_2 = f'{sleep_type} - {cost:.2f}'
print(out_line_1)
print(out_line_2)
