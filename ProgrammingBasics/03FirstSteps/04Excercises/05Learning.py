# •	Пакет химикали - 5.80 лв.
price_pens = 5.80
# •	Пакет маркери - 7.20 лв.
price_markers = 7.2
# •	Препарат - 1.20 лв (за литър)
price_detergent = 1.2

# От конзолата се четат 4 числа:
# •	Брой пакети химикали - цяло число в интервала [0...100]
count_pens = int(input())
# •	Брой пакети маркери - цяло число в интервала [0...100]
count_markers = int(input())
# •	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
count_detergent = int(input())
# •	Процент намаление - цяло число в интервала [0...100]
discount_percent = int(input())

# total amount
total = round(price_pens * count_pens + price_markers * count_markers + price_detergent * count_detergent, 2)
discount = round(total * discount_percent / 100, 2)
cost = round(total - discount, 2)
print(cost)
