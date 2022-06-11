n = int(input())  # >=0
m = int(input())  # >= n
s = int(input())  # between m and n

delta = m % 6
m -= delta
if m < n:
    exit()
for i in range(m, n - 1, -6):
    if i != s:
        print(i, end=' ')
    else:
        break
