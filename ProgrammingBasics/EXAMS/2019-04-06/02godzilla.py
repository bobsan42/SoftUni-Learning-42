x = input()
budget = float(x)
x = input()
actors = int(x)
x = input()
price_clothes = float(x)
clothes = actors * price_clothes
if actors > 150:
    clothes *= .9
decor = .1 * budget
cost = decor + clothes
diff = abs(budget - cost)

# print(f'{cost:.2f}')
if cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
