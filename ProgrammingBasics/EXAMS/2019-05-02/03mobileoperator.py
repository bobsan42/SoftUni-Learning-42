contract_types_list = ["Small", "Middle", "Large", "ExtraLarge"]
one_year_prices_list = [9.98, 18.99, 25.98, 35.99]
two_year_prices_list = [8.58, 17.09, 23.59, 31.79]

contract_duration = input()
contract_type = input()
mobile_internet = input()
number_of_months_to_pay = int(input())

monthly_price = 0
idx = contract_types_list.index(contract_type)

if contract_duration == 'one':
    monthly_price = one_year_prices_list[idx]
elif contract_duration == 'two':
    monthly_price = two_year_prices_list[idx]

if mobile_internet == 'yes':
    if monthly_price > 30:
        monthly_price += 3.85
    elif monthly_price > 10:
        monthly_price += 4.35
    else:
        monthly_price += 5.50

if contract_duration == 'two':
    monthly_price *= (1 - .0375)
total_cost = monthly_price * number_of_months_to_pay

print(f'{total_cost:.2f} lv.')
