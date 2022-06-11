from math import ceil

figure_size = int(input())
mid = ceil(figure_size / 2)
for i in range(1, figure_size + 1):
    if i == 1 or i == figure_size:
        print('*' * 2 * figure_size + ' ' * figure_size + '*' * 2 * figure_size)
    elif i == mid:
        print('*' + '/' * (2 * figure_size - 2) + '*' + '|' * figure_size + '*' + '/' * (2 * figure_size - 2) + '*')
    else:
        print('*' + '/' * (2 * figure_size - 2) + '*' + ' ' * figure_size + '*' + '/' * (2 * figure_size - 2) + '*')
