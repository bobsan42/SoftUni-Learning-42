# По време на обедната почивка искате да изгледате епизод от своя любим сериал.
# Вашата задача е да напишете програма, с която ще разберете дали имате достатъчно време да изгледате епизода.
# По време на почивката отделяте време за обяд и време за отдих.
# Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
# 1.	Име на сериал – текст
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
# Изход
# На конзолата да се изпише един ред:
# •	Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
# •	Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
from math import ceil

ser_name = input()
ser_duration = int(input())
br_duration = int(input())

t_lunch = br_duration / 8
t_rest = br_duration / 4
time_to_watch = br_duration - t_rest - t_lunch
delta = ceil(abs(ser_duration - time_to_watch))
if time_to_watch < ser_duration:
    print(f'You don\'t have enough time to watch {ser_name}, '
          f'you need {delta} more minutes.')
else:
    print(f'You have enough time to watch {ser_name} '
          f'and left with {delta} minutes free time.')
