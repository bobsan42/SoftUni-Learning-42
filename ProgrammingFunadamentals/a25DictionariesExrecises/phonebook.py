def phone_book():
    phonebook = {}
    while True:
        str = input()
        if not '-' in str:
            break
        data = str.split('-')
        phonebook[data[0]] = data[1]
        # name, phone = str.split('-')
        # phonebook[name]=phone

    for _ in range(int(str)):
        name = input()
        if name in phonebook.keys():
            print(f'{name} -> {phonebook[name]}')
        else:
            print(f'Contact {name} does not exist.')


phone_book()
