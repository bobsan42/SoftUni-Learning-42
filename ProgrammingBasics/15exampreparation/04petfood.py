n_days = int(input())
qty_all_food = float(input())
dog_food_eaten = 0
cat_food_eaten = 0
biscuits_eaten = 0

for i in range(1, n_days + 1):
    dog_daily_food = int(input())
    cat_daily_food = int(input())
    dog_food_eaten += dog_daily_food
    cat_food_eaten += cat_daily_food
    if i % 3 == 0:
        biscuits_eaten += 0.10 * (dog_daily_food + cat_daily_food)

total_food_eaten = dog_food_eaten + cat_food_eaten
biscuits_eaten = int(round(biscuits_eaten, 0))

print(f"Total eaten biscuits: {biscuits_eaten}gr.")
print(f"{(total_food_eaten / qty_all_food * 100):.2f}% of the food has been eaten.")
print(f"{(dog_food_eaten / total_food_eaten * 100):.2f}% eaten from the dog.")
print(f"{(cat_food_eaten / total_food_eaten * 100):.2f}% eaten from the cat.")
