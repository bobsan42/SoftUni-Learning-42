x = input()
if x == 'Monday' or x == 'Tuesday' or x == 'Wednesday' or x == 'Thursday' or x == 'Friday':
    y = "Working day"
elif x == 'Saturday' or x == 'Sunday':
    y = 'Weekend'
else:
    y = 'Error'

print(y)
