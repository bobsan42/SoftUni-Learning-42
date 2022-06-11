budget = float(input())
n = int(input())
m = int(input())
p = int(input())

nn = n * 250
mm = .35 * nn
pp = .1 * nn
cost = nn + mm * m + pp * p
if n > m:
    cost = .85 * cost
if cost > budget:
    print(f'Not enough money! You need {(cost - budget):.2f} leva more!')
else:
    print(f'You have {(budget - cost):.2f} leva left!')
