x = input()
# x = 'abbababxxba'
# x = 'abc'
longest_palindrome = ''
if len(x) == 2:
    if x[0] == x[1]:
        longest_palindrome = x
elif len(x) == 1:
    longest_palindrome = x
elif len(x) > 2:
    # odd length
    for i in range(1, len(x) - 1):
        pal = x[i]
        if len(pal) > len(longest_palindrome):
            longest_palindrome = pal
        distance_to_end = min(len(x) - i - 1, i)
        for offset in range(1, distance_to_end + 1):
            if x[i - offset] == x[i + offset]:
                pal = x[i - offset:i + offset + 1]
                if len(pal) > len(longest_palindrome):
                    longest_palindrome = pal
                # print(pal)
            else:
                break
    # even length
    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            pal = x[i:i + 2]
            if len(pal) > len(longest_palindrome):
                longest_palindrome = pal
        else:
            continue
        distance_to_end = min(len(x) - i - 2, i)
        for offset in range(1, distance_to_end + 1):
            if x[i - offset] == x[(i + 1) + offset]:
                pal = x[i - offset:(i + 1) + offset + 1]
                if len(pal) > len(longest_palindrome):
                    longest_palindrome = pal
                # print(pal)
            else:
                break
# print ('the longest palingrome is:',longest_palindrome)
print(len(longest_palindrome))
