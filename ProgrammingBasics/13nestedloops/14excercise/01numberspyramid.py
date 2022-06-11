n = int(input())
row = 1
col = 0

for i in range(1, n + 1):
    print(i, end=' ')
    col += 1
    if col == row:
        row += 1
        col = 0
        print()
