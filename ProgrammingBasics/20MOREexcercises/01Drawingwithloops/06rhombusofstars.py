char = '* '
figure_size = int(input())

for i in range(1, figure_size + 1):
    leader = " " * (figure_size - i)
    print(leader + char * i)
for i in range(figure_size - 1, 0, -1):
    leader = " " * (figure_size - i)
    print(leader + char * i)
