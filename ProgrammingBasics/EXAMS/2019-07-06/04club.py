target_revenue = float(input())
command = 'Party!'
n_cocktails = 0
money_collected = 0
diff = target_revenue - money_collected
are_collected = False
order = input()

while order != command:
    n_order = int(input())
    order_price = len(order) * n_order
    if order_price % 2 == 1:
        order_price *= .75
    money_collected += order_price
    if money_collected >= target_revenue:
        are_collected = True
        break
    else:
        diff = target_revenue - money_collected
    order = input()

if are_collected:
    print("Target acquired.")
else:
    print(f"We need {diff:.2f} leva more.")

print(f"Club income - {money_collected:.2f} leva.")
