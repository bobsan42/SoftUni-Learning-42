n_sites = int(input())

for i in range(n_sites):
    expected_daily_extraction = float(input())
    n_days_on_site = int(input())
    gold_collected = 0
    for j in range(n_days_on_site):
        gold_for_the_day = float(input())
        gold_collected += gold_for_the_day
    average_daily_production = gold_collected / n_days_on_site
    if average_daily_production < expected_daily_extraction:
        diff = expected_daily_extraction - average_daily_production
        print(f"You need {diff:.2f} gold.")
    else:
        print(f"Good job! Average gold per day: {average_daily_production:.2f}.")
