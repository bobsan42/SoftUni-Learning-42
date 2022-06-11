char = '$'
figure_size = int(input())
for i in range(figure_size):
    for j in range(i+1):
        if j == 0:
            print(char, end='')
        else:
            print(' ' + char, end='')
    print()