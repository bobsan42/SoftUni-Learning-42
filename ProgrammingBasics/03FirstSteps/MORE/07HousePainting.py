# Напишете програма, която да пресмята колко литра боя е нужна за боядисването на къщa.
# Като за стените се използва зелена боя, а за покрива – червена.
# Разхода на зелената боя е 1 литър за 3.4 м2, а на червената – 1 литър за 4.3 м2.
razhod_zel = 1 / 3.4  # l/m2
razhod_red = 1 / 4.3  # l/m2

# Вход
# От конзолата се четат 3 реда:
# 1.	x – височината на къщата – реално число в интервала [2...100]
x = float(input())
# 2.	y – дължината на страничната стена – реално число в интервала [2...100]
y = float(input())
# 3.	h – височината на триъгълната стена на прокрива – реално число в интервала [2...100]
h = float(input())

# Стените имат следните размери:
# •	Предната и задната стена са квадрати със страна „x“
# o	на предната стена има правоъгълна врата с широчина 1.2м и височина 2м
walls1 = 2 * x * x - 1.2 * 2
# •	Страничните стени са правоъгълници със страни „x“ и „y“
# o	и на двете странични стени има по един квадратен прозорец със страна 1.5м
walls2 = 2 * (x * y - 1.5 * 1.5)
zel = razhod_zel * (walls1 + walls2)

# Покривът има следните размери:
# •	Два правоъгълника със страни „x“ и „y“
roof1 = 2 * x * y
# •	Два равностранни триъгълника със страна „x“ и височина „h“
roof2 = 2 * (x * h / 2)
# Трябва да пресметнете площта на всички страни и площта на покрива, за да
# намерите колко литра от всяка боя ще са нужни.
red = razhod_red * (roof1 + roof2)

# Изход
# Да се отпечатат на конзолата две числа всяко на нов ред:
# •	Литрите зелена боя
print(f'{zel:.2f}')
# •	Литритe червена боя
print(f'{red:.2f}')
# Форматирани до вторият знак след десетичната запетая.
