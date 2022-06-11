n_start = int(input())
n_end = int(input())

for num in range(n_start, n_end + 1):
    num_str = str(num)
    odd_sum = 0
    even_sum = 0
    for idx, digit in enumerate(num_str):
        if idx % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if odd_sum == even_sum:
        print(num_str, end=' ')
