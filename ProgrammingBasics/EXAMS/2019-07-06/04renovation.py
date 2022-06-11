from math import ceil

n_walls = 4
paint_per_sq_m = 1  # l/m2
wall_height = int(input())
wall_width = int(input())
wall_no_paint_percent = int(input())
wall_no_paint_percent /= 100
command = "Tired!"
area_painted = 0
area_to_paint = ceil(4 * wall_height * wall_width * (1 - wall_no_paint_percent))
area_left = area_to_paint
operation = input()

while operation != command:
    paint = int(operation)
    area = paint / paint_per_sq_m
    area_painted += area
    area_left = area_to_paint - area_painted
    if area_left <= 0:
        break
    operation = input()

if area_left == 0:
    print("All walls are painted! Great job, Pesho!")
elif area_left < 0:
    diff = ceil(abs(area_left * paint_per_sq_m))
    print(f"All walls are painted and you have {diff:.0f} l paint left!")
else:
    print(f"{area_left:.0f} quadratic m left.")
