num = int(input())
stack = []
for _ in range(num):
    qry = input()
    if qry == '2':
        if len(stack) > 0:
            stack.pop()
    elif qry == '3':
        if len(stack) > 0:
            print(max(stack))
    elif qry == '4':
        if len(stack) > 0:
            print(min(stack))
    elif qry[0] == '1':
        stack.append(int(qry.split(' ')[1]))
result = []
while len(stack) > 0:
    result.append(str(stack.pop()))
print(', '.join(result))
