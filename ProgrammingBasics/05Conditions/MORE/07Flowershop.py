from math import ceil, floor

n_magnolia = int(input())
n_zyumbyul = int(input())
n_roses = int(input())
n_cactus = int(input())
gift_price = float(input())

total_sale = \
    n_magnolia * 3.25 + \
    n_zyumbyul * 4 + \
    n_roses * 3.50 + \
    n_cactus * 8
after_taxes = total_sale * .95
diff = abs(after_taxes - gift_price)

if after_taxes < gift_price:
    print(f'She will have to borrow {ceil(diff)} leva.')
else:
    print(f'She is left with {floor(diff)} leva.')
