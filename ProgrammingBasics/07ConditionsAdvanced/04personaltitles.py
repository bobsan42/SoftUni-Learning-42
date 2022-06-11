age = float(input())
gender = input()

if gender == 'm':
    if age < 16:
        x = 'Master'
    else:
        x = 'Mr.'
elif gender == 'f':
    if age < 16:
        x = 'Miss'
    else:
        x = 'Ms.'
print(x)
