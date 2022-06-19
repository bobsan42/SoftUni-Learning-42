def divider(list_to_divide, list_index: int, partitions: int):
    # Divides an element from the list to the given number of partitions
    # #####################################################
    # Every time you receive the divide command,
    # you must divide the element at the given index into several small substrings with equal length.
    # The count of the substrings should be equal to the given partitions.
    # Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
    # If the string cannot be exactly divided into the given partitions,
    # make all partitions except the last with equal lengths and make the last one - the longest.
    # Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
    divide_result = []
    for idx, x in enumerate(list_to_divide, ):
        if idx != list_index:
            divide_result.append(x)
        else:
            length = len(x) // partitions
            i = 0
            for _ in range(partitions - 1):
                i = _
                divide_result.append(x[0 + length * i:length + length * i])
            divide_result.append(x[0 + length * (i+1):])

    return divide_result


my_list = ['a', 'frogstomp42', 'b', 'c', 'd', 'e', 'f']
result = divider(my_list, 1, 3)
print(' '.join(result))
