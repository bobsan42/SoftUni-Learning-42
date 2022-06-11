# from math import floor

t1 = int(input())
t2 = int(input())
t3 = int(input())
tt = t1 + t2 + t3
# tmin = floor(tt // 60)
tsec = "{:02d}".format(tt % 60)
print(f'{tmin}:{tsec}')
