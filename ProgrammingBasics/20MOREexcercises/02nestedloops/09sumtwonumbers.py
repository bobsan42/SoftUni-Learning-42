int_start = int(input())
int_end = int(input())
target_sum = int(input())

is_found = False
count_combinations = (int_end - int_start + 1) ** 2
min_target = 2 * int_start
max_target = 2 * int_end
# if min_target <= target_sum <= max_target:
if target_sum in range(min_target, max_target):
    count_combinations = 0
    for x in range(int_start, int_end + 1):
        if is_found:
            break
        for y in range(int_start, int_end + 1):
            count_combinations += 1
            if x + y == target_sum:
                print(f'Combination N:{count_combinations} ({x} + {y} = {target_sum})')
                is_found = True
                break

if not is_found:
    print(f'{count_combinations} combinations - neither equals {target_sum}')
