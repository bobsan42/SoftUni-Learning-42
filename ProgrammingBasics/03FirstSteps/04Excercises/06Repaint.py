# •	Предпазен найлон - 1.50 лв. за кв. метър
price_nylon = 1.50
# •	Боя - 14.50 лв. за литър
price_paint = 14.50
# •	Разредител за боя - 5.00 лв. за литър
price_solvent = 5
# За всеки случай, към необходимите материали:
# Румен иска да добави още 10% от количеството боя
factor_paint = 1.1
# 2 кв.м. найлон
factor_nylon_add = 2
# разбира се и 0.40 лв. за торбички
cost_bags = 0.40
# Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали.
factor_labor_per_hour = 0.30
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
# 1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
qty_nylon = int(input())
# 2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
qty_paint = int(input())
# 3.	Количество разредител (в литри) - цяло число в интервала [1…30]
qty_solvent = int(input())
# 4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
qty_labor = int(input())

cost_nylon = (qty_nylon + factor_nylon_add) * price_nylon
cost_paint = (qty_paint * factor_paint) * price_paint
cost_solvent = qty_solvent * price_solvent
cost_materials = cost_paint + cost_nylon + cost_solvent + cost_bags
price_labor = factor_labor_per_hour * cost_materials
cost_labor = price_labor * qty_labor

# Изход
# Да се отпечата на конзолата един ред:
# •	"{сумата на всички разходи}"
print(cost_materials + cost_labor)
