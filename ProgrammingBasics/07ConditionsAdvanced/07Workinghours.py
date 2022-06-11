h = int(input())
d = input()

if h < 10 or h >= 18:
    x = 'closed'
else:
    if d == 'Sunday':
        x = 'closed'
    else:
        x = 'open'
print(x)
