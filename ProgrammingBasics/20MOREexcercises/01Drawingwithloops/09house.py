figure_size = int(input())
roof_lines = int((figure_size + 1) / 2)
body_lines = int(figure_size / 2)
x = '*'
y = '|'
z = '-'
n = figure_size - (roof_lines - 1) * 2
for i in range(1, roof_lines + 1):
    m = n + (i - 1) * 2
    k = int((figure_size - m) / 2)
    print(z * k + x * m + z * k)

m = figure_size - 2
for i in range(1, body_lines + 1):
    print(y + x * m + y)
