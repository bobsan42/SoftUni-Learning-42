# n = int(input())
#
# # for row in range(1, n+1):
# #     print("* " * row)
# #
# # for row in range(n-1, -1,-1):
# #     print("* " * row)
# for row in range(1, n+1):
#
#
# for row in range(n-1,-1,-1):
#     print(' '*(n-row),end='')
#     for col in range(1, row+1):
#         print("* ", end="")
#     print()


def draw_rhombus(size, symbol='*'):
    for row in range(1, size + 1):
        print_row(size, row, symbol)

    for row in range(size - 1, -1, -1):
        print_row(size, row, symbol)


def print_row(figure_size, row_size, symbol):
    print(' ' * (figure_size - row_size), end='')
    for col in range(1, row_size + 1):
        print(symbol, end=" ")
    print()


n = int(input())

symbol_to_use = '@'
draw_rhombus(n, symbol_to_use)
