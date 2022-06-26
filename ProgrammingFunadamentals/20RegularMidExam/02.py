# COFFEE LOVER

johns_coffees = input()
coffees_list = johns_coffees.split()
n = int(input())  # commands count


def edit_coffee_list(list_command):
    cmd = list_command.split()
    if cmd[0] == 'Include':
        coffees_list.append(cmd[1])
    elif cmd[0] == 'Remove':
        items_to_remove = int(cmd[2])
        if items_to_remove > len(coffees_list):
            return
        if cmd[1] == 'first':
            i = 0
        elif cmd[1] == 'last':
            i = -1
        for _ in range(items_to_remove):
            coffees_list.pop(i)
    elif cmd[0] == 'Prefer':
        coffee_index_1 = int(cmd[1])
        coffee_index_2 = int(cmd[2])
        if coffee_index_1 > len(coffees_list) - 1:
            return
        if coffee_index_2 > len(coffees_list) - 1:
            return
        coffees_list[coffee_index_1], coffees_list[coffee_index_2] = \
            coffees_list[coffee_index_2], coffees_list[coffee_index_1]
    elif cmd[0] == 'Reverse':
        coffees_list.reverse()


for _ in range(n):
    command = input()
    edit_coffee_list(command)
    # print(coffees_list)

print('Coffees:')
# print(coffees_list)
print(' '.join(coffees_list))
