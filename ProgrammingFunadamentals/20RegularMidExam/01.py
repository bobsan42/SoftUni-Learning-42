import math

# Cooking Masterclass
# one student package:
# 1 package of flour
# 10 eggs
# 1 apron

budget = float(input())
students = int(input())
flour_pack_price = float(input())  # every fifth package is free
an_egg_price = float(input())
apron_price = float(input())  # increase aprons by 20% because they get dirty

total_cost = students * (
        flour_pack_price + 10 * an_egg_price + apron_price
)
# increase aprons by 20% because they get dirty
total_cost += math.ceil(students / 5) * apron_price
# every fifth package is free
total_cost -= (students // 5) * flour_pack_price
diff = (total_cost - budget)

# # Driver code
# if __name__ == '__main__':
#     # function call
#     ...
if total_cost > budget:
    print(f'{diff:.2f}$ more needed.')
else:
    print(f'Items purchased for {total_cost:.2f}$.')
