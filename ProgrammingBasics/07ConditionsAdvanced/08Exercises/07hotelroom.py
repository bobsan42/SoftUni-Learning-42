month_name = input()
num_nights = int(input())

price_studio = 0  # price per night
price_apt = 0
if month_name == 'May' or month_name == 'October':
    price_apt = 65
    if num_nights > 14:
        price_studio = 50 * .7
    elif num_nights > 7:
        price_studio = 50 * .95
    else:
        price_studio = 50
elif month_name == 'June' or month_name == 'September':
    price_apt = 68.70
    if num_nights > 14:
        price_studio = 75.20 * .8
    else:
        price_studio = 75.20
elif month_name == 'July' or month_name == 'August':
    price_studio = 76
    price_apt = 77

if num_nights > 14:
    price_apt *= .9

cost_apt = num_nights * price_apt
cost_studio = num_nights * price_studio
out_apt = f'Apartment: {cost_apt:.2f} lv.'
out_studio = f'Studio: {cost_studio:.2f} lv.'

print(out_apt)
print(out_studio)
