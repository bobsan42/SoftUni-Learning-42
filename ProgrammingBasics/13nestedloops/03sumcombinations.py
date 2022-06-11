target_sum = int(input())
combo_count = 0
# x1 + x2 + x3 = target_sum
# x1,2,3 - natural numbers

for x1 in range(0, target_sum + 1):
    for x2 in range(0, target_sum + 1):
        s2 = x1 + x2
        if s2 > target_sum:
            break
        for x3 in range(0, target_sum + 1):
            s3 = s2 + x3
            if s3 == target_sum:
                combo_count += 1
                break
print(combo_count)
