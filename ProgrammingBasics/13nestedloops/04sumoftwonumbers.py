int_start = int(input())
int_end = int(input())
target_sum = int(input())
is_found = False
combinations_count = 0
x1 = 0
x2 = 0
if int_start * 2 > target_sum > int_end * 2:
    combinations_count = (int_end - int_start + 1) ** 2
else:
    for a in range(int_start, int_end + 1):
        if is_found:
            break
        for b in range(int_start, int_end + 1):
            combinations_count += 1
            # is_found = ((a + b) == target_sum)
            if (a + b) == target_sum:
                is_found = True
                x1 = a
                x2 = b
                break
if is_found:
    print(f'Combination N:{combinations_count} ({x1} + {x2} = {target_sum})')
else:
    # •	Ако не е намерена комбинация отговаряща на условието
    print(f'{combinations_count} combinations - neither equals {target_sum}')
