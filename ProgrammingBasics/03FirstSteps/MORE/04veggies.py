bgn_to_eur = 1.94
# •	Първи ред – Цена за килограм зеленчуци – реално число[0.00… 1000.00]
price_veggies = float(input())
# •	Втори ред – Цена за килограм плодове – реално число[0.00… 1000.00]
price_fruits = float(input())
# •	Трети ред – Общо килограми на зеленчуците – цяло число[0… 1000]
qty_veggies = int(input())
# •	Четвърти ред – Общо килограми на плодовете – цяло число[0… 1000]
qty_fruits = int(input())

revenue = qty_fruits * price_fruits + \
          qty_veggies * price_veggies

print('{:.2f}'.format(revenue / bgn_to_eur))
