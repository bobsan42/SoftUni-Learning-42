months_of_the_year = ["January", "February", "March",
                      "April", "May", "June",
                      "July", "August", "September",
                      "October", "November", "December"]
days_in_each_month = [31, 28, 31,
                      30, 31, 30,
                      31, 31, 30,
                      31, 30, 31]
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
first_weekday_occurrence = [0, 0, 0, 0, 0, 0, 0]

first_day_of_the_month = int(input("Enter first weekday of the year: (number 1 to 7)"))
print(f'First weekday is {days_of_the_week[first_day_of_the_month - 1]}')
is_leap_year = bool(input("Is this a leap year? (y/n)").lower() == 'y')

if is_leap_year:
    days_in_each_month[1] = 29
print('The firs weekday of ...')
for idx, month in enumerate(months_of_the_year):
    print(f'{month} is {first_day_of_the_month} ({days_of_the_week[first_day_of_the_month - 1]})')
    first_weekday_occurrence[first_day_of_the_month - 1] += 1
    first_day_of_the_month += days_in_each_month[idx] % 7
    if first_day_of_the_month > 7:
        first_day_of_the_month -= 7

print('First month\'s weekday occurrence:' )
for idx, day in enumerate(days_of_the_week):
    print(f'    {day}s: {first_weekday_occurrence[idx]}')