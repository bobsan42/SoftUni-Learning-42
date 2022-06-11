# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ.
# Напишете програма, която спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече.
# Вашият приятел има различни планове за всеки етап от деня,
# които изискват и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# •	Градусите - цяло число;
# •	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
grad = int(input())
daytime = input()
outfit = ''
shoes = ''
clothes = 0
if daytime == 'Morning':
    if grad > 24:
        clothes = 3
    elif grad > 18:
        clothes = 2
    elif grad >= 10:
        clothes = 1
elif daytime == 'Afternoon':
    if grad > 24:
        clothes = 4
    elif grad > 18:
        clothes = 3
    elif grad >= 10:
        clothes = 2
elif daytime == 'Evening':
    if grad > 24:
        clothes = 2
    elif grad > 18:
        clothes = 2
    elif grad >= 10:
        clothes = 2

if clothes == 1:
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
elif clothes == 2:
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif clothes == 3:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif clothes == 4:
    outfit = 'Swim Suit'
    shoes = 'Barefoot'

print(f"It's {grad} degrees, get your {outfit} and {shoes}.")

# Време от денонощието / градуси
# Morning
# Afternoon
# Evening
# 10 <= градуси <= 18	Outfit = Sweatshirt
# Shoes = Sneakers	Outfit = Shirt
# Shoes = Moccasins	Outfit = Shirt
# Shoes = Moccasins
# 18 < градуси <= 24	Outfit = Shirt
# Shoes = Moccasins	Outfit = T-Shirt
# Shoes = Sandals	Outfit = Shirt
# Shoes = Moccasins
# градуси >= 25	Outfit = T-Shirt
# Shoes = Sandals	Outfit = Swim Suit
# Shoes = Barefoot	Outfit = Shirt
# Shoes = Moccasins

# Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."
