# Напишете програма, която проследява представянето на вашия отбор на благотворителен коледен турнир.
# Всеки ден получавате имена на игри до команда "Finish".
# Със спечелването на всяка една игра печелите по 20лв. за благотворителност.
# Трябва да изчислите колко пари сте спечелили на края на деня.
# Ако имате повече спечелени игри, отколкото загубени – вие сте победители този ден и увеличавате парите от него с 10%.
# При приключване на турнира, ако през повечето дни сте били победители,
#   печелите турнира и увеличавате всичките спечелени пари с 20%.
# Никога няма да имате равен брой спечелени и загубени игри.

# Вход
# Първоначално от конзолата се прочита броя дни на турнира – цяло число в интервала [1… 20]
n_days = int(input())
# До получаване на командата "Finish" се чете:
# •	Спорт  – текст
money_won = 0
# games_won = 0
# games_lost = 0
win_days = 0
loose_days = 0

for i in range(n_days):
    day_won = 0
    day_lost = 0
    day_money = 0
    sport = input()
    while sport != 'Finish':
        # За всеки спорт се прочита:
        # o	Резултат  – текст с възможности: "win" или "lose"
        result = input()
        if result == 'win':
            # day_money +=20
            day_won += 1
        else:
            day_lost += 1
        sport = input()
    day_money = 20 * day_won
    if day_won > day_lost:
        day_money *= 1.1
        win_days += 1
    else:
        loose_days += 1
    money_won += day_money
    # games_won += day_won
    # games_lost += day_lost

# Изход
# Накрая се отпечатва един ред:
if win_days > loose_days:
    # •	Ако сте спечелили турнира:
    money_won *= 1.2
    print(f"You won the tournament! Total raised money: {money_won:.2f}")
else:
    # •	Ако сте загубили на турнира:
    print(f"You lost the tournament! Total raised money: {money_won:.2f}")
# Парите да бъдат форматирани до втората цифра след десетичния знак.
