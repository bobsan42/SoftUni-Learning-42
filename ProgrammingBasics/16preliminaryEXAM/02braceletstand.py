days_remaining = 5

pocket_money_per_day = float(input())
profit_per_day = float(input())
all_expenses = float(input())
gift_price = float(input())

total_savings = days_remaining * (profit_per_day + pocket_money_per_day) - all_expenses
diff = (gift_price - total_savings)

if diff > 0:
    print(f"Insufficient money: {diff:.2f} BGN.")
else:
    print(f"Profit: {total_savings:.2f} BGN, the gift has been purchased.")
