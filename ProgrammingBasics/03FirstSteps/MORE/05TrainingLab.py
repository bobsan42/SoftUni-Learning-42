w = float(input())  # length
h = float(input())  # width

n_w = (w * 100) // 120
n_h = (h * 100 - 100) // 70

n = n_w * n_h - 1 - 2
print(int(n))
