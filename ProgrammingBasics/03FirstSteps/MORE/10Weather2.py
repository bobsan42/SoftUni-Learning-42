x = float(input())
y = 'unknown'
if 5 <= x <= 11.9:
    y = 'Cold'
elif 12 <= x <= 14.9:
    y = 'Cool'
elif 15 <= x <= 20:
    y = 'Mild'
elif 20.1 <= x <= 25.9:
    y = "Warm"
elif 26 <= x <= 35:
    y = "Hot"
print(y)
