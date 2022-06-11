# В кутия имаме неопределен брой топки с различни цветове, които ни носят различен брой точки. Задачата ни е да извадим Х бр. топки, които ще бъдат въведени от конзолата, като се има в предвид, че всеки различен цвят влияе на точките ни по следния начин:
# •	Ако топката е “red” точките ни се повишават с 5.
# •	Ако топката е “orange” точките ни се повишават с 10.
# •	Ако топката е “yellow” точките ни се повишават с 15.
# •	Ако топката е “white” точките ни се повишават с 20.
# •	Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число.
# Ако топката е с какъвто и да е цвят, различен от по-горните, точките не се манипулират и програмата продължава да работи.
# Вход:
# 1.	От конзолата се чете 1 цяло число N, което е броят на топките в диапазон (0-1000).
# 2.	След това се четат N на брой цветове.
n = int(input())
nred = 0
norng = 0
nyell = 0
nwhite = 0
nblack = 0
nother = 0

points = 0
for i in range(n):
    color = input()
    if color == 'red':
        points += 5
        nred += 1
    elif color == 'orange':
        points += 10
        norng += 1
    elif color == 'yellow':
        points += 15
        nyell += 1
    elif color == 'white':
        points += 20
        nwhite += 1
    elif color == 'black':
        points = int(points / 2)
        nblack += 1
    else:
        nother += 1
        pass

# Изход:
# Отпечатват се следните редове:
print(f"Total points: {points}")
print(f"Red balls: {nred}")
print(f"Orange balls: {norng}")
print(f"Yellow balls: {nyell}")
print(f"White balls: {nwhite}")
print(f"Other colors picked: {nother}")
print(f"Divides from black balls: {nblack}")
