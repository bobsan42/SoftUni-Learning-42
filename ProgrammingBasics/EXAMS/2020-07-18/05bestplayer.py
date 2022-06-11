# Задача 5. Най-добър играч
# Пепи иска да напишете програма, чрез която да разбере кой е най-добрият играч от световното първенство.
# Информацията, която получавате ще бъде играч и колко гола е отбелязал.
# От вас се иска да отпечатате кой е играчът с най-много голове и дали е направил хет-трик.
# Хет-трик е, когато футболистът е вкарал 3 или повече гола.
# Ако футболистът е вкарал 10 или повече гола, програмата трябва да спре.
# Вход:
# От конзолата се четат по два реда до въвеждане на команда "END":
# •	Име на играч – текст
# •	Брой вкарани голове  – цяло положително число в интервала [1 … 10000]
# Изход:
# На конзолата да се отпечатат 2 реда :
# •	На първия ред:
#             "{име на играч} is the best player!"
# •	На втория ред :
# o	 Ако най-добрият футболист е направил хеттрик:
#                    "He has scored {брой голове} goals and made a hat-trick !!!"
# o	Ако най-добрият футболист не е направил хеттрик:
#                    "He has scored {брой голове} goals."
best_player = ''
best_score = 0
hat_trick = False

player = input()
while player != 'END':
    score = int(input())
    if score > best_score:
        best_player = player
        best_score = score
        hat_trick = (score > 2)
    if score >= 10:
        break
    player = input()
print(f'{best_player} is the best player!')
if hat_trick:
    print(f'He has scored {best_score} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_score} goals.')
