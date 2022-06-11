n = int(input())  # figure size
x = '*'
y = '-'

n_half_lines = int((n - 1) / 2)
n_x = 2 - (n % 2)
n_y_end = int((n - n_x) / 2)
n_y_mid = n % 2

print(y * n_y_end + x * n_x + y * n_y_end)
if n > 2:
    for i in range(2, n_half_lines + 1):
        print(y * (n_y_end - i + 1) + x + y * ((i - 1) * 2 - n_y_mid) + x + y * (n_y_end - i + 1))
    print(x + y * (n - 2) + x)
    for i in range(n_half_lines, 1, -1):
        print(y * (n_y_end - i + 1) + x + y * ((i - 1) * 2 - n_y_mid) + x + y * (n_y_end - i + 1))
    print(y * n_y_end + x * n_x + y * n_y_end)
