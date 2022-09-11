initial_string = input()
current_string = initial_string


def replace_cmd(currentChar, newChar):
    global current_string
    result = current_string.replace(currentChar, newChar)
    current_string = result
    print(result)


def cut_cmd(startIndex, endIndex):
    global current_string
    if startIndex < 0 or startIndex >= len(current_string):
        result = "Invalid indices!"
        print(result)
        return
    elif endIndex < 0 or endIndex >= len(current_string):
        result = "Invalid indices!"
        print(result)
        return

    # if abs(startIndex) >= len(current_string) or \
    #         abs(endIndex) >= len(current_string):
    #     result = "Invalid indices!"
    #     print(result)
    #     return
    if endIndex < len(current_string) - 1:
        result = current_string[:startIndex]  + current_string[endIndex + 1:]
    else:
        result = current_string[:startIndex]
    current_string = result
    print(result)


def make_cmd(case: str):
    global current_string
    result = current_string
    if case == 'Upper':
        result = current_string.upper()
    elif case == 'Lower':
        result = current_string.lower()
    current_string = result
    print(result)


def check_cmd(check_string: str):
    global current_string
    if check_string in current_string:
        print(f'Message contains {check_string}')
    else:
        print(f"Message doesn't contain {check_string}")


def sum_ascii(startIndex, endIndex):
    global current_string
    if startIndex < 0 or startIndex >= len(current_string):
        result = "Invalid indices!"
        print(result)
        return
    elif endIndex < 0 or endIndex >= len(current_string):
        result = "Invalid indices!"
        print(result)
        return
    x = [ord(ch) for ch in current_string[startIndex:endIndex]]
    x.append(ord(current_string[endIndex]))
    print(sum(x))


command = ''
while True:
    command = input()
    if command == "Finish":
        break
    c = command.split(" ")
    if c[0] == 'Replace':
        replace_cmd(c[1], c[2])
    elif c[0] == 'Cut':
        cut_cmd(int(c[1]), int(c[2]))
    elif c[0] == 'Make':
        make_cmd(c[1])
    elif c[0] == 'Check':
        check_cmd(c[1])
    elif c[0] == 'Sum':
        sum_ascii(int(c[1]), int(c[2]))
