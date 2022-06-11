divisors_list = [2, 3, 4]
divisors_count_list = [0, 0, 0]

numbers_to_check = int(input())

for i in range(numbers_to_check):
    x = int(input())
    for idx, div in enumerate(divisors_list):
        divisors_count_list[idx] += int(x % div == 0)

for counted in divisors_count_list:
    print(f'{(counted / numbers_to_check * 100):.2f}%')
