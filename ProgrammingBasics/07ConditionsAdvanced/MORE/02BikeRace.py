# Предстои Вело състезание за благотворителност в което участниците са разпределени
# в младша("juniors") и старша("seniors") група.
# Парите се набавят от таксата за участие на велосипедистите.
# Според възрастовата група и вида на трасето на което ще се провежда състезанието, таксата е различна.
# Група	trail	cross-country	downhill	road
# juniors	5.50	8	12.25	20
# seniors	7	9.50	13.75	21.50
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши),
# таксата  намалява с 25%. Организаторите отделят 5% процента от събраната сума за разходи.

# Вход
# От конзолата се четат 2 числа и един стринг, всяко на отделен ред:
# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
n_juniors = int(input())
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
n_seniors = int(input())
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
trace_type = input()
price_jun = 0
price_sen = 0
if trace_type == 'trail':
    price_jun = 5.50
    price_sen = 7
elif trace_type == 'cross-country':
    red = .75 if (n_seniors + n_juniors) >= 50 else 1
    price_jun = 8 * red
    price_sen = 9.50 * red
    # if n_seniors+n_juniors>=50:
    #     price_jun=.75*price_jun
    #     price_sen=.75*price_sen
elif trace_type == 'downhill':
    price_jun = 12.25
    price_sen = 13.75
elif trace_type == 'road':
    price_jun = 20
    price_sen = 21.5
taxes = n_seniors * price_sen + n_juniors * price_jun
expenses = .05 * taxes

# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.
print(f'{(taxes * .95):.2f}')
