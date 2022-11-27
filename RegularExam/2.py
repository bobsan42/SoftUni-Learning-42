# Rally Racing
# https://judge.softuni.org/Contests/Compete/Index/3596#1

matrix_size = int(input())
car_number = input()

race_matrix = []
car_position = [0, 0]
row_position = 0
col_position = 0
distance_covered = 0  # km
delta_move = 10  # km
delta_tunnel = 30  # km
disqualified = False

for _ in range(matrix_size):
    line = list(input().split())
    race_matrix.append(line)

tunnel_end_1 = [] # [row,col]
tunnel_end_2 = [] # [row,col]
finish_position = [] # [row,col]

for i in range(matrix_size):
    for j in range(matrix_size):
        cell_value = race_matrix[i][j]
        if cell_value == "F":
            finish_position = [i,j]
        elif cell_value == "T":
            if len (tunnel_end_1) == 0:
                tunnel_end_1 = [i,j]
            else:
                tunnel_end_2 = [i,j]

while True:
    command = input()
    if command == "End":
        disqualified = True
        break
    dr = 0
    dc = 0
    if command == "left":
        dc = -1
    elif command == "right":
        dc =1
    elif command == "up":
        dr = -1
    elif command == "down":
        dr = 1
    col_position += dc
    row_position += dr

    char = race_matrix[row_position][col_position]
    if char == ".":
        distance_covered +=10
    elif char == "F":
        distance_covered +=10
        break
    elif char == "T":
        distance_covered += 30
        race_matrix[row_position][col_position] = "."
        if [row_position,col_position] == tunnel_end_1:
            row_position = tunnel_end_2[0]
            col_position = tunnel_end_2 [1]
        else:
            row_position = tunnel_end_1[0]
            col_position = tunnel_end_1 [1]
        race_matrix[row_position][col_position] = "."




race_matrix[row_position][col_position] = "C"

if disqualified:
    print(f"Racing car {car_number} DNF.")
else:
    print(f"Racing car {car_number} finished the stage!")

print(f"Distance covered {distance_covered} km.")

for i in range(matrix_size):
    for j in range(matrix_size):
        print(race_matrix[i][j], end="")
    print()

