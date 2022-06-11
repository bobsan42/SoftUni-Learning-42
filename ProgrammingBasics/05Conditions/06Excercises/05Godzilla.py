budget = float(input())
stats = int(input())
clothes_price = float(input())
decor = budget * .1
clothes = stats * clothes_price
if stats > 150:
    clothes = clothes * .9
cost = clothes + decor
# На конзолата трябва да се отпечатат два реда:
# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
# •	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.
if cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {(cost - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget - cost):.2f} leva left.")
