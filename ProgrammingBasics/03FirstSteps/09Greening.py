# import math

area=float(input()) # a number btw 0.00 and 1000.00
pDisc=0.18
uPrice = 7.61
cost = area*uPrice
disc = cost *pDisc
total = cost-disc


print(f'The final price is: {total} lv.')
print(f'The discount is: {disc} {{lv}}.')