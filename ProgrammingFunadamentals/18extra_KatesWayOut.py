can_get_out = True
is_in = True
the_maze = []
moves_made = 0
init_position = [0, 0]
k_position = [0, 0]  # [row, column]
maze_rows = 0
maze_columns = 0


def check_adjacent_cells():
    for step in range(-1, 2, 2):
        cell = the_maze[k_position[0] + step][k_position[1]]
        if cell == ' ':
            return [k_position[0] + step, k_position[1]]
    for step in range(-1, 2, 2):
        cell = the_maze[k_position[0]][k_position[1] + step]
        if cell == ' ':
            return [k_position[0], k_position[1] + step]
    return False


def print_the_maze():
    for row in the_maze:
        print(''.join(row))


def kate_s_way_out():
    # get out of the maze
    global k_position, can_get_out, is_in
    global maze_rows
    global maze_columns
    global the_maze
    global moves_made

    maze_rows = int(input())
    # •	"#" - means a wall; Kate cannot go through there
    # •	" " - means empty space; Kate can go through there
    # •	"k" - the initial position of Kate; start looking for a way out from there
    # There are two options: Kate either gets out or not:
    # •	If Kate can get out, print the following:  "Kate got out in {number_of_moves} moves".
    # •	Otherwise, print: "Kate cannot get out".
    # Note: If there are two or more ways out, she always chooses the longest one.

    for _ in range(maze_rows):
        the_maze.append(list(input()))
    maze_columns = len(the_maze[0])
    # print_the_maze()

    for row in the_maze:
        if 'k' in row:
            init_position[0] = the_maze.index(row)
            init_position[1] = row.index('k')
            break
    the_maze[init_position[0]][init_position[1]] = 'v'
    k_position = init_position.copy()

    # print(init_position)

    while can_get_out and is_in:
        # visited cells will be marked with 'v'
        if k_position[0] == 0 or k_position[0] == maze_rows - 1 \
                or k_position[1] == 0 or k_position[1] == maze_columns - 1:
            # this is the edge so escape one step away
            moves_made += 1
            break
            # assume that there will be no position outside the maze

        next_cell = check_adjacent_cells()

        if next_cell == False:
            # No more moves from this position
            can_get_out = False
            pass
        else:
            k_position = next_cell.copy()
            the_maze[k_position[0]][k_position[1]] = 'v'
            moves_made += 1

        # print_the_maze()
    # some cheating
    for row in the_maze:
        moves_made += row.count(' ')

    if not can_get_out:
        print('Kate cannot get out')

    else:
        print(f'Kate got out in {moves_made} moves')


# Driver code
if __name__ == '__main__':
    # function call
    kate_s_way_out()
