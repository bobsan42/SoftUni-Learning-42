rate_evenday_oddhour = 2.50
rate_oddday_evenhour = 1.25
rate_general = 1

n_days = int(input())
n_hours_per_day = int(input())
total_to_pay = 0
pay_per_day = 0
x = 0
for d in range(1, n_days + 1):
    pay_per_day = 0
    for h in range(1, n_hours_per_day + 1):
        if d % 2 == 0 and h % 2 == 1:
            x = rate_evenday_oddhour
        elif d % 2 == 1 and h % 2 == 0:
            x = rate_oddday_evenhour
        else:
            x = rate_general
        pay_per_day += x
        total_to_pay += x
    print(f'Day: {d} - {pay_per_day:.2f} leva')

print(f'Total: {total_to_pay:.2f} leva')
