# Вход:
# От конзолата се четат 4 реда:
# 1. Цената на багаж над 20кг - реално число в диапазона [10.0...80.0]
# 2. Килограми на багажа – реално число в диапазона [1.0...32.0]
# 3. Дни до пътуването – цяло число в диапазона [1...60]
# 4. Брой багажи – цяло число в диапазона [1...10]
price_over_20kg = float(input())
luggage_kg = float(input())
days_remaining = int(input())
bags_number = int(input())
bag_fee = 0
total_cost = 0

if 10 > luggage_kg:
    bag_fee = 0.2 * price_over_20kg
elif 20 >= luggage_kg >= 10:
    bag_fee = 0.5 * price_over_20kg
elif luggage_kg > 20:
    bag_fee = price_over_20kg

if days_remaining > 30:
    bag_fee *= 1.1
elif 30 >= days_remaining >= 7:
    bag_fee *= 1.15
elif days_remaining < 7:
    bag_fee *= 1.4
total_cost = bag_fee * bags_number

print(f'The total price of bags is: {total_cost:.2f} lv.')
