field = []
connectable_dots = 0
n_rows = int(input())
all_chains = []
current_chain = []
# recursion_level = 0

for _ in range(n_rows):
    row = input().split()
    # row = list(map(int, row))
    field.append(row)
max_row = n_rows - 1
max_col = len(field[0]) - 1


def is_connected(coordinates: list):
    if coordinates in current_chain:
        return True
    for chain in all_chains:
        if coordinates in chain:
            return True
    return False


def make_chain(coordinates: list, level: int):
    global current_chain
    if not is_connected(coordinates):
        current_chain.append(coordinates)
    else:
        return

    r = coordinates[0]  # row index
    c = coordinates[1]  # column index

    if r > 0:
        x = field[r - 1][c]
        if x == '.':
            make_chain([r - 1, c], level + 1)
    if r < max_row:
        x = field[r + 1][c]
        if x == '.':
            make_chain([r + 1, c], level + 1)
    if c > 0:
        x = field[r][c - 1]
        if x == '.':
            make_chain([r, c - 1], level + 1)
    if c < max_col:
        x = field[r][c + 1]
        if x == '.':
            make_chain([r, c + 1], level + 1)

    if level == 0:
        all_chains.append(current_chain)
        current_chain = []


for i in range(max_row + 1):
    for j in range(max_col + 1):
        if field[i][j] == '.':
            make_chain([i, j], 0)

# print(all_chains)
max_connectable_dots = 0
for chain in all_chains:
    if len(chain) > max_connectable_dots:
        max_connectable_dots = len(chain)
print(max_connectable_dots)
# print(connectable_dots)
