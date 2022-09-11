user_capacity = int(input())
manager = {}  # {username:[sent,received]]


def add_cmd(username: str, sent_msgs: int, received_msgs: int):
    if username not in manager.keys():
        manager[username] = [sent_msgs, received_msgs]
        return True
    else:
        return False


def message(sender: str, recipient: str):
    x = [sender, recipient]
    for y in x:  # check if both users exist
        if y not in manager.keys():
            return

    for idx in range(2):  # add message to sent/received counters
        manager[x[idx]][idx] += 1

    for idx in range(2):  # check i user capacity exceeded
        if sum(manager[x[idx]]) >= user_capacity:
            manager.pop(x[idx])  # remove user if capacity exceeded
            print(f"{x[idx]} reached the capacity!")  # print message


def empty_cmd(username: str):
    if username == 'All':
        manager.clear()
        return
    if username in manager.keys():
        manager[username] = []
        manager.pop(username)
        return True
    else:
        return False


while True:
    command = input()
    if command == "Statistics":
        break
    command = command.split("=")
    cmd = command[0]
    if cmd == "Add":
        add_cmd(command[1], int(command[2]), int(command[3]))
    elif cmd == 'Message':
        message(command[1], command[2])
    elif cmd == 'Empty':
        empty_cmd(command[1])

print(f"Users count: {len(manager.keys())}")
for (user, messages) in manager.items():
    print(f'{user} - {sum(messages)}')
