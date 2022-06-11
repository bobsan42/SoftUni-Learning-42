food_bought = int(input())  # kg
food_remaining = food_bought * 1000  # gr
data_entry = input()
while data_entry != "Adopted":
    food_remaining -= int(data_entry)
    data_entry = input()
if food_remaining < 0:
    print(f"Food is not enough. You need {abs(food_remaining)} grams more.")
else:
    print(f"Food is enough! Leftovers: {food_remaining} grams.")
