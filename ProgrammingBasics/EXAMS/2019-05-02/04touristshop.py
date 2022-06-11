budget = float(input())
money_left = budget
product_counter = 0
not_enough_money = False

product_name = input()
while product_name != 'Stop':
    product_counter += 1
    product_price = float(input())
    if product_counter % 3 == 0:
        product_price /= 2
    if product_price > money_left:
        not_enough_money = True
        money_left = abs(product_price - money_left)
        product_counter -= 1
        break
    money_left -= product_price
    product_name = input()

if not_enough_money:
    print("You don't have enough money!")
    print(f"You need {money_left:.2f} leva!")
else:
    print(f"You bought {product_counter} products for {(budget - money_left):.2f} leva.")
