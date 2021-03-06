# Студент трябва да пропътува n километра. Той има избор измежду три вида транспорт:

# •	Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.

# •	Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.

# •	Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.

# Напишете програма, която въвежда броя километри n и период от деня (ден или нощ) и изчислява цената на най-евтиния транспорт.
# Вход
# От конзолата се четат два реда:
# •	Първият ред съдържа числото n – брой километри – цяло число в интервала [1…5000]
dist = int(input())
# •	Вторият ред съдържа дума “day” или “night” – пътуване през деня или през нощта
day = input()
# Изход
# Да се отпечата на конзолата най-ниската цена за посочения брой километри, форматирана до втория знак след десетичния разделител.
dt = 1 if day == 'day' else 0
nt = 1 if day == 'night' else 0
taxi = .7 + (dt * .79 + nt * .90) * dist
bus = .09 * dist
train = .06 * dist
if dist < 20:
    x = taxi
elif dist < 100:
    x = min(taxi, bus)
else:
    x = min(taxi, bus, train)
print("{:.2f}".format(x))
