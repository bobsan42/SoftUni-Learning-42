import re

pattern = '![A-Z][a-z]{2}[a-z]*!:\[[a-zA-Z]{8}[a-zA-Z]*\]'


def check_command(command):
    global pattern
    x = re.findall(pattern, command)
    # print(x)
    if len(x) > 0:
        return x[0]
    else:
        print('The message is invalid')
        return None


def translate(command: str):
    a = command.split('!:[')
    cmd = a[0][1:]
    msg = a[1][:-1]
    print(cmd, end=': ')
    for c in msg:
        print(ord(c),end=' ')
    print()


n = int(input())
for _ in range(n):
    command = input()
    # y = check_command('sd sdsd !Send!:[IvanisHere]d asd asd ')
    y = check_command(command)
    if y is not None:
        translate(y)
