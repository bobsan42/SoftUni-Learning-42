budget = float(input())
n_nights = int(input())
price_per_night = float(input())
additional_expences = int(input())
additional_expences = budget * (additional_expences / 100)
if n_nights > 7:
    price_per_night *= .95
total_cost = price_per_night * n_nights + additional_expences
diff = abs(total_cost - budget)

if total_cost > budget:
    print(f'{diff:.2f} leva needed.')
else:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
