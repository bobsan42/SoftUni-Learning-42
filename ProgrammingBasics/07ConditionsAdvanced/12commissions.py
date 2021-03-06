# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
# Град	0 ≤ s ≤ 500	500 < s ≤ 1 000	1 000 < s ≤ 10 000	s > 10 000
# Sofia	5%	7%	8%	12%
# Varna	4.5%	7.5%	10%	13%
# Plovdiv	5.5%	8%	12%	14.5%
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".
grad = input()
sale = float(input())

com = 0
if sale >= 0:
    if grad == 'Sofia':
        if sale <= 500:
            com = 5
        elif sale <= 1000:
            com = 7
        elif sale <= 10000:
            com = 8
        elif sale > 10000:
            com = 12
    elif grad == 'Varna':
        if sale <= 500:
            com = 4.5
        elif sale <= 1000:
            com = 7.5
        elif sale <= 10000:
            com = 10
        elif sale > 10000:
            com = 13
    elif grad == 'Plovdiv':
        if sale <= 500:
            com = 5.5
        elif sale <= 1000:
            com = 8
        elif sale <= 10000:
            com = 12
        elif sale > 10000:
            com = 14.5
if com == 0:
    print('error')
else:
    rev = sale * com / 100
    print(f'{rev:.2f}')
