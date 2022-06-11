sp = float(input())
if sp <= 10:
    x = 'slow'
else:
    if sp <= 50:
        x = 'average'
    else:
        if sp <= 150:
            x = 'fast'
        else:
            if sp <= 1000:
                x = 'ultra fast'
            else:
                x = 'extremely fast'
print(x)
