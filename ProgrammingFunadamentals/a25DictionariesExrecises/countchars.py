def count_chars():
    characters = {}
    list_chars = list(input())
    for x in list_chars:
        if x == ' ':
            continue
        if not x in characters.keys():
            characters[x] = 0
        characters[x] += 1

    for (char, count) in characters.items():
        print(f"{char} -> {count}")


count_chars()
