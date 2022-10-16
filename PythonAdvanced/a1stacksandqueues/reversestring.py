# text1 = input()
text1 = 'I Love Python'
lst = list(text1)
result = []
while len(lst) >0:
    chr = lst.pop()
    print(chr,end='')
print()
# option 2
text1 = 'I Love Python'
lst = list(text1)
result = []
while len(lst) >0:
    result.append(lst.pop())
print(''.join(result))