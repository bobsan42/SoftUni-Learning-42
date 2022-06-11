# •	Първи ред - напитка - текст с възможности"Espresso", "Cappuccino" или "Tea"
# •	Втори ред - захар - текст  с възможности "Without", "Normal" или "Extra"
# •	Трети ред - брой напитки - цяло число в интервала [1… 50]
drink = input()  # "Espresso", "Cappuccino" или "Tea"
sugar = input()  # "Without", "Normal" или "Extra"
n_drinks = int(input())
price = 0
discount = 0
if drink == "Espresso":
    if sugar == "Without":
        price = .9
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.2
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.2
    elif sugar == "Extra":
        price = 1.6
elif drink == "Tea":
    if sugar == "Without":
        price = .5
    elif sugar == "Normal":
        price = .6
    elif sugar == "Extra":
        price = .7
if sugar == 'Without':
    price *= .65
cost = n_drinks * price
if drink == 'Espresso' and n_drinks > 4:
    cost *= .75
if cost > 15:
    cost *= .8

print(f'You bought {n_drinks} cups of {drink} for {cost:.2f} lv.')
