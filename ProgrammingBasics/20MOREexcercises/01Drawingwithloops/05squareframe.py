char = '- '
corner = '+ '
vert_side = '| '

rectangle_size = int(input())
rect_width = rectangle_size  # 10
rect_height = rectangle_size  # 10

for i in range(rect_height):
    if i==0 or  i==rect_height-1:
        print(corner + char*(rect_width-2) +corner)
    else:
        print(vert_side + char * (rect_width - 2) + vert_side)
    # print()
