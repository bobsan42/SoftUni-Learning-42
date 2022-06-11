# Задача 5. Товарене на багажи
# Напишете програма, която ви помага при товаренето на куфари в багажника на самолет.
# Всеки самолет има определен капацитет на багажника. До получаване на команда "End" ще получавате обем на куфар.
# Обемът на всеки трети куфар трябва да се увеличава с 10%, поради загубата на пространство при начина на подреждане.
# Ако свободното пространството в даден момент е по-малко от обема на куфар товаренето трябва да прекъсне.
# TODO:
#   something is not working properly in some specific case;
#   test here: https://judge.softuni.org/Contests/Practice/Index/2275#9

# Вход
# Първоначално се чете един ред:
# •	Капацитетът на багажника – реално число в диапазона [100.0…6000.0]
capacity = float(input())
free_space = capacity
added_suitcase_volume = input()
count_suitcases = 0
is_full = False
is_ended = False
x = 0.0
# След това до получаване на команда "End" или до запълване на багажника, се чете по един ред:
# o	Обем на куфар – реално число в диапазона [100.0…6000.0]
if added_suitcase_volume.lower() == 'end':
    is_ended = True
# else:
#     x = float(added_suitcase_volume)

while True:
    if is_ended:
        break
    x = float(added_suitcase_volume)
    if (count_suitcases +1) % 3 ==0:
        x *= 1.1
    free_space -= x
    if free_space <0:
        is_full = True
        # if free_space==0:
        #     count_suitcases += 1
        break
    count_suitcases += 1
    added_suitcase_volume = input()
    if added_suitcase_volume.lower() == 'end':
        is_ended = True
        break

# Изход
# На конзолата да се отпечатат следните редове според случая:
if is_ended:
    # •	При получаване на командата "End" се печата:
    print("Congratulations! All suitcases are loaded!")
else:
    # •	Ако обемът на куфара е по-голям от оставащото пространство в багажника:
    print("No more space!")
# •	Накрая винаги се отпечатва статистика – колко багажа са натоварени:
print(f"Statistic: {count_suitcases:.0f} suitcases loaded.")


# #####################################################################
# ## VERSION 1: 80/100
# #####################################################################
# # Задача 5. Товарене на багажи
# # Напишете програма, която ви помага при товаренето на куфари в багажника на самолет.
# # Всеки самолет има определен капацитет на багажника. До получаване на команда "End" ще получавате обем на куфар.
# # Обемът на всеки трети куфар трябва да се увеличава с 10%, поради загубата на пространство при начина на подреждане.
# # Ако свободното пространството в даден момент е по-малко от обема на куфар товаренето трябва да прекъсне.
#
# # Вход
# # Първоначално се чете един ред:
# # •	Капацитетът на багажника – реално число в диапазона [100.0…6000.0]
# capacity = float(input())
# free_space = capacity
# suitcase_volume = input()
# count_suitcases = 0
# is_full = False
# # След това до получаване на команда "End" или до запълване на багажника, се чете по един ред:
# # o	Обем на куфар – реално число в диапазона [100.0…6000.0]
# while suitcase_volume != 'End':
#     x = float(suitcase_volume)*1.1
#     if free_space < x:
#         is_full = True
#         break
#     free_space -= x
#     count_suitcases += 1
#     suitcase_volume = input()
# # Изход
# # На конзолата да се отпечатат следните редове според случая:
# if not is_full:
#     # •	При получаване на командата "End" се печата:
#     print("Congratulations! All suitcases are loaded!")
# else:
#     # •	Ако обемът на куфара е по-голям от оставащото пространство в багажника:
#     print("No more space!")
# # •	Накрая винаги се отпечатва статистика – колко багажа са натоварени:
# print(f"Statistic: {count_suitcases} suitcases loaded.")
