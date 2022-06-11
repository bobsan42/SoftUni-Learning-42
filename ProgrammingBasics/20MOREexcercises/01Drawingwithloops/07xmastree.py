symbol_1 = ' | '
symbol_2 = '*'
figure_size = int(input())
for i in range(figure_size + 1):
    leader = " " * (figure_size - i)
    print(leader + symbol_2 * i + symbol_1 + symbol_2 * i)
