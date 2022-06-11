# Вход
# От конзолата се четат 4 реда:
# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].
season = input()
sex = input()
n_students = int(input())
n_nights = int(input())

# Частно училище организира лагери за учениците по време на ваканциите.
# В зависимост от вида на ваканцията (пролетна, лятна или зимна) и вида на групата (момчета/момичета или смесена)
# цената на нощувката в хотела е различна, както и спортът, който ще практикуват учениците.
# 	Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момчета/момичета	9.60	7.20	15
# смесена група	10	9.50	20
price = 0
if season == 'Winter':
    if sex == 'boys' or sex == 'girls':
        price = 9.60
    elif sex == 'mixed':
        price = 10
elif season == 'Spring':
    if sex == 'boys' or sex == 'girls':
        price = 7.20
    elif sex == 'mixed':
        price = 9.50
elif season == 'Summer':
    if sex == 'boys' or sex == 'girls':
        price = 15
    elif sex == 'mixed':
        price = 20

# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка
discount = 0
cost = n_students * n_nights * price
if n_students >= 50:
    discount = .5
elif n_students >= 20:
    discount = .15
elif n_students >= 10:
    discount = .05
cost = cost * (1 - discount)
# В таблицата по-долу са дадени спортовете, които ще се практикуват в зависимост от вида на ваканцията и групата:
# 	Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момичета	Gymnastics	Athletics	Volleyball
# момчета	Judo	Tennis	Football
# смесена група	Ski	Cycling	Swimming
if season == 'Winter':
    if sex == 'girls':
        sport = 'Gymnastics'
    elif sex == 'boys':
        sport = 'Judo'
    elif sex == 'mixed':
        sport = 'Ski'
elif season == 'Spring':
    if sex == 'girls':
        sport = 'Athletics'
    elif sex == 'boys':
        sport = 'Tennis'
    elif sex == 'mixed':
        sport = 'Cycling'
elif season == 'Summer':
    if sex == 'girls':
        sport = 'Volleyball'
    elif sex == 'boys':
        sport = 'Football'
    elif sex == 'mixed':
        sport = 'Swimming'

# Да се напише програма, която пресмята цената, която ще заплати училището за нощувките и принтира спорта,
# който ще се практикува от учениците.
# Изход
# На конзолата се отпечатва 1 ред:
# •	Спортът, който са практикували учениците и цената за нощувките, която е заплатило училището,
# форматирана до втория знак след десетичната запетая, в следния формат:
# "{спортът} {цената} lv.“
print(f'{sport} {cost:.2f} lv.')
