# Напишете програма, която спрямо даден бюджет и сезон да пресмята цената, типа и класа на кола под наем.
# Вход
# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – Бюджет – реално число в интервала [10.00...10000.00]
budget = float(input())
# •	Втори ред –  Сезон – текст "Summer" или "Winter"
season = input()

# Сезоните са лято и зима – "Summer" и "Winter". Типа коли са кабрио и джип – "Cabrio" и "Jeep".
# •	При бюджет по-малък или равен от 100лв.:
if budget <= 100:
    # o	Класът ще е - "Economy class"
    car_class = "Economy class"
    # o	Според сезона колата и цената ще са:
    if season == 'Summer':
        # 	Лято – Кабрио – 35% от бюджета
        car_type = "Cabrio"
        car_price = .35 * budget
    else:
        # 	Зима – Джип – 65% от бюджета
        car_type = "Jeep"
        car_price = .65 * budget
elif budget <= 500:
    # •	При бюджет по-голям от 100лв. и по-малък или равен от 500лв.:
    # o	Класът ще е - "Compact class"
    car_class = 'Compact class'
    # o	Според сезона колата и цената ще са:
    if season == 'Summer':
        # 	Лято – Кабрио – 45% от бюджета
        car_type = "Cabrio"
        car_price = .45 * budget
    else:
        # 	Зима – Джип – 80% от бюджета
        car_type = "Jeep"
        car_price = .80 * budget
elif budget > 500:
    # •	При бюджет по-голям от 500лв.:
    # o	Класът ще е – "Luxury class"
    car_class = "Luxury class"
    # o	За всеки сезон колата ще е джип и цената ще е:
    # 	90% от бюджета
    car_type = "Jeep"
    car_price = .90 * budget

# Изход
# На конзолата трябва да се отпечатат два реда.
# •	Първи ред – "{Вид на класа}"
# o	"Economy class", "Compact class" или "Luxury class"
print(car_class)
# •	Втори ред – "{Вид на колата} - {цена на колата}"
# o	Видът на колата – "Cabrio" или "Jeep"
# o	Цената трябва да е форматирана до втория знак след запетаята
print(f'{car_type} - {car_price:.2f}')
