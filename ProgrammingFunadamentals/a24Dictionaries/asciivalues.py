def ascii_values():
    some_letters = input().split(', ')
    my_dict= {char:ord(char) for char in some_letters}
    print(my_dict)

ascii_values()