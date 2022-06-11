#   От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.

t_flower = input()
n_flower = int(input())
budget = int(input())

price = 0
discount = 0
if t_flower == "Roses":
    price = 5
    if n_flower > 80:
        discount = -10
elif t_flower == "Dahlias":
    price = 3.80
    if n_flower > 90:
        discount = -15
elif t_flower == "Tulips":
    price = 2.80
    if n_flower > 80:
        discount = -15
elif t_flower == "Narcissus":
    price = 3
    if n_flower < 120:
        discount = +15
elif t_flower == "Gladiolus":
    price = 2.50
    if n_flower < 80:
        discount = +20

cost = n_flower * price * (1 + discount / 100)
diff = abs(budget - cost)

if cost > budget:
    print(f'Not enough money, you need {diff:.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {n_flower} {t_flower} and {diff:.2f} leva left.')

# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

