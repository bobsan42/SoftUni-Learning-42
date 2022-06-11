num = int(input())
bonus = 0
if num <= 100:
    bonus = 5
elif num > 1000:
    bonus = num * .1
else:
    bonus = num * .2

if (num % 2) == 0:
    bonus = bonus + 1
# elif (num % 5) == 0:
elif (num % 5) == 5:
    bonus = bonus + 2

print(bonus)
print(num + bonus)
