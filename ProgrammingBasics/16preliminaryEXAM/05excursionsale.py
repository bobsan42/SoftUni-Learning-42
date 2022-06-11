type_package_1 = "sea"
type_package_2 = "mountain"
price_package_1 = 680
price_package_2 = 499

n_package_1 = int(input())
n_package_2 = int(input())
remaining_package_1 = n_package_1
remaining_package_2 = n_package_2
all_sold = False
sales_package_1 = 0
sales_package_2 = 0

package = input()
while package != 'Stop':
    if package == type_package_1:
        if remaining_package_1 > 0:
            sales_package_1 += price_package_1
            remaining_package_1 -= 1
    elif package == type_package_2:
        if remaining_package_2 > 0:
            sales_package_2 += price_package_2
            remaining_package_2 -= 1
    if remaining_package_2 + remaining_package_1 == 0:
        all_sold = True
        break
    package = input()
if all_sold:
    print('Good job! Everything is sold.')
print(f'Profit: {(sales_package_1 + sales_package_2)} leva.')
