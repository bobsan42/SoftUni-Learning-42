n1 = int(input())
n2 = int(input())
oper = input()

oper_string = f'{n1} {oper} {n2}'
if n2 == 0 and (oper == '/' or oper == '%'):
    res = f"Cannot divide {n1} by zero"
else:
    x = eval(oper_string)
    if oper == "+" or oper == "*" or oper == '-':
        if x % 2 == 0:
            res = ' - even'
        else:
            res = ' - odd'
        res = f'{oper_string} = {x}{res}'
    elif oper == '%':
        res = f'{oper_string} = {x}'
    elif oper == '/':
        res = f'{oper_string} = {x:.2f}'
print(res)
