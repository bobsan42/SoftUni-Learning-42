# •	Първи ред - дни за престой - цяло число в интервала [0...365]
# •	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment"
# •	Трети ред - оценка - "positive"  или "negative"
n_days = int(input())
room_type = input()
review = input()

n_nights = n_days - 1  # брой нощувки
discount = 0
price = 0
if room_type == "room for one person":
    price = 18.00  # лв за нощувка
elif room_type == "apartment":
    price = 25.00
    if n_days < 10:
        discount = -30
    elif n_days <= 15:
        discount = -35
    elif n_days > 15:
        discount = -50
elif room_type == "president apartment":
    price = 35.00
    if n_days < 10:
        discount = -10
    elif n_days <= 15:
        discount = -15
    elif n_days > 15:
        discount = -20
price_correction = 0
if review == 'positive':
    price_correction = +25
elif review == 'negative':
    price_correction = -10
cost = n_nights * price * (1 + discount / 100) * (1 + price_correction / 100)
print(f'{cost:.2f}')
