destinations_list = ["Bansko", "Borovets", "Varna", "Burgas"]
packages_list = ["withEquipment", "noEquipment", "withBreakfast", "noBreakfast"]
destination = input()
package = input()
has_vip = input()
number_of_days = int(input())

# check input
if number_of_days < 1:
    print("Days must be positive number!")
    exit()
if has_vip != 'yes' and has_vip != 'no':
    print("Invalid input!")
    exit()
if destination not in destinations_list:
    print("Invalid input!")
    exit()
if package not in packages_list:
    print("Invalid input!")
    exit()
idx_destination = destinations_list.index(destination)
idx_package = packages_list.index(package)
# if idx_package > 1 and idx_destination < 2:
#     exit("Invalid input!")
# if idx_package < 2 and idx_destination > 1:
#     exit("Invalid input!")

price_per_day = 0
vip_discount = 0
if idx_destination < 2:
    if idx_package == 0:
        price_per_day = 100
        vip_discount = 10
    elif idx_package == 1:
        price_per_day = 80
        vip_discount = 5
    else:
        print("Invalid input!")
        exit()

elif idx_destination > 1:
    if idx_package == 2:
        price_per_day = 130
        vip_discount = 12
    elif idx_package == 3:
        price_per_day = 100
        vip_discount = 7
    else:
        print("Invalid input!")
        exit()
if number_of_days > 7:
    number_of_days -= 1
total_cost = number_of_days * price_per_day
if has_vip == 'yes':
    total_cost = total_cost * (100 - vip_discount) / 100

print(f"The price is {total_cost:.2f}lv! Have a nice time!")
