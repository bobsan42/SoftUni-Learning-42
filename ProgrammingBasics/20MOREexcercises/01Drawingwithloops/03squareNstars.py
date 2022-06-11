char = '*'
rectangle_size = int(input())
rect_width = rectangle_size  # 10
rect_height = rectangle_size  # 10
for i in range(rect_height):
    for j in range(rect_width):
        if j == 0:
            print(char, end='')
        else:
            print(' ' + char, end='')
    print()
