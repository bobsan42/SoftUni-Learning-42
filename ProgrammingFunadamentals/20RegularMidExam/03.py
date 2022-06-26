# THE ANGRY CAT

price_ratings = input()
items_ratings_list = list(map(int, price_ratings.split(', ')))
entry_point = int(input())  # index between the second and the penultimate element in the list
type_to_break = input()
# target_price = items_ratings_list[entry_point]
damage_list = [0, items_ratings_list[entry_point], 0]  # [left of entry, entry point rating, right of entry]

for i in [-1, 1]:
    for item in items_ratings_list[entry_point + i::i]:
        if type_to_break == 'cheap' and item < damage_list[1]:
            damage_list[1 + i] += item
        elif type_to_break == 'expensive' and item >= damage_list[1]:
            damage_list[1 + i] += item

if damage_list[2] > damage_list[0]:
    result = f'Right - {damage_list[2]}'
else:
    result = f'Left - {damage_list[0]}'

# print(damage_list)
print(result)
