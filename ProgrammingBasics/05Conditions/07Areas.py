from math import pi

f1 = 'square'
f2 = 'rectangle'
f3 = 'circle'
f4 = 'triangle'

fig = input()
a = float(input())
if fig == f2 or fig == f4:
    b = float(input())
if fig == f1:
    x = a * a
if fig == f2:
    x = a * b
if fig == f3:
    x = pi * a * a
if fig == f4:
    x = a * b / 2
x = round(x, 3)
print("{:.3f}".format(x))
