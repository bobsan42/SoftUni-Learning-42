# Вход:
# Потребителят въвежда 3 реда:
# 1.	Брой дограми – цяло число в интервала [0..1000];
# 2.	Вид на дограмите – текст "90X130" или "100X150" или "130X180" или "200X300";
# 3.	Начин на получаване – текст
# •	С доставка - "With delivery"
# •	Без доставка - "Without delivery"
d_count = int(input())
d_type = input()
d_deliver_method = input()
delivery_fee = 60 if d_deliver_method == 'With delivery' else 0
unit_price = 0
percent_discount = 0
if d_count < 10:
    print('Invalid order')
else:
    # Изход:
    # Извежда се едно число – стойността на поръчката, в следния формат:
    # Резултатът да се форматира до втори знак след десетичната запетая.
    if d_type == "90X130":
        unit_price = 110
        if d_count > 30:
            percent_discount = 5
        if d_count > 60:
            percent_discount = 8
    elif d_type == "100X150":
        unit_price = 140
        if d_count > 40:
            percent_discount = 6
        if d_count > 80:
            percent_discount = 10
    elif d_type == "130X180":
        unit_price = 190
        if d_count > 20:
            percent_discount = 7
        if d_count > 50:
            percent_discount = 12
    elif d_type == "200X300":
        unit_price = 250
        if d_count > 25:
            percent_discount = 9
        if d_count > 50:
            percent_discount = 14
    unit_price *= (1 - percent_discount / 100)
    total_order = d_count * unit_price + delivery_fee
    if d_count > 99:
        total_order *= .96
    print(f"{total_order:.2f} BGN")
