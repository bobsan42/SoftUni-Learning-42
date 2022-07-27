force_book = {}  # {side: [users]}


def get_user_side(username: str):
    for (side, users) in force_book.items():
        if username in users:
            return side
    return None


def change_side(username, move_to_side):
    current_side = get_user_side(username)
    if current_side is not None:
        force_book[current_side].remove(username)
    if move_to_side not in force_book.keys():
        force_book[move_to_side] = []
    force_book[move_to_side].append(username)

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    case = 0
    # user = ''
    # side = ''
    for i in range(1, 3):
        if i == 1:
            splitter = ' | '  # "{force_side} | {force_user}"
        else:
            splitter = ' -> '  # "{force_user} -> {force_side}"
        data = command.split(splitter)
        if len(data) == 2:
            case = i
            user = data[0 - i]
            side = data[1 - i]
            user_side = get_user_side(user)
            break
    if case == 0:
        print('BAD INPUT: ', command)
    if case == 1:
        if user_side is not None:
            continue
        if side not in force_book.keys():
            force_book[side] = []
        if user_side is None:
            force_book[side].append(user)
    elif case == 2:
        change_side(user, side)
        print(f'{user} joins the {side} side!')

for (side, users) in force_book.items():
    if len(users) == 0:
        continue
    print(f"Side: {side}, Members: {len(users)}")
    for user in users:
        print(f'! {user}')
