# numbers_list = input().split(", ")
# result = 0
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number < 5:
#         result *= number
#     elif number > 5 and number > 10:
#         result /= number
# print(result)

# input: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# calculation: 1*2*3*4*5/6/7/8/9/10
# expected result: 0.003968253968253968

numbers_list = input().split(", ")
result = 1
for i in (numbers_list):
    number = int(i)
    if number <= 5:
        result *= number
    elif number > 5 and number < 11:
        result /= number
print(result)

# option 2:
numbers_list = [int(x) for x in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif number > 5 and number <= 10:
        result /= number

print(result)
