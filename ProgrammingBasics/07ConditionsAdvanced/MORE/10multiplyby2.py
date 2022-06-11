n = 0
while n >= 0:
    n = float(input())
    if n < 0:
        print('Negative number!')
    else:
        print(f'Result: {(n * 2):.2f}')
