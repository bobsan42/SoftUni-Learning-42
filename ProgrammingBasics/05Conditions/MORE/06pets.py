from math import ceil,floor
days = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turt_food_per_day = float(input())

tot_food = days * (dog_food_per_day + cat_food_per_day + turt_food_per_day/1000)

if food_left >=tot_food:
    print(f'{floor(food_left-tot_food)} kilos of food left.')
else:
    print(f'{ceil(tot_food-food_left)} more kilos of food are needed.')