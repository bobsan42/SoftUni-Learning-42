calories_in_fats = 9
calories_in_proteins = 4
calories_in_carbohydrates = 4

percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())

total_calories = int(input())
percent_water = int(input())

weight_fats = percent_fats * total_calories / calories_in_fats
weight_proteins = percent_proteins * total_calories / calories_in_proteins
weight_carbohydrates = percent_carbohydrates * total_calories / calories_in_carbohydrates
total_food_weight = weight_fats + \
                    weight_proteins + \
                    weight_carbohydrates

calories_in_one_gram_food = total_calories / total_food_weight * (100 - percent_water)  # *100/100

print(f'{calories_in_one_gram_food:.4f}')
