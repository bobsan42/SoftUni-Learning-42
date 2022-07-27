users = {}

def register(username: str, license_plate: str):
    if username in users.keys():
        print(f'ERROR: already registered with plate number {license_plate}')
    else:
        users[username] =  license_plate
        print(f'{username} registered {license_plate} successfully')


def unregister(username: str):
    if username not in users.keys():
        print(f'ERROR: user {username} not found')
    else:
        print(f'{username} unregistered successfully')
        users.pop(username)


def print_users():
    for (user, plate) in users.items():
        print(f'{user} => {plate}')


def su_parking():
    n = int(input())
    for _ in range(n):
        command = input().split(' ')
        if command[0] == 'register':
            register(command[1], command[2])
        elif command[0] == 'unregister':
            unregister(command[1])
    print_users()

# Driver code
if __name__ == '__main__':
    # function call
    su_parking()
