title = input()
hall_type = input()
n_tickets = int(input())
revenue = 0
price = 0
movies = ["A Star Is Born", "Bohemian Rhapsody", "Green Book", "The Favourite"]
halls = ['normal', 'luxury', 'ultra luxury']

if title == movies[0]:
    if hall_type == halls[0]:
        price = 7.50
    elif hall_type == halls[1]:
        price = 10.50
    elif hall_type == halls[2]:
        price = 13.50
elif title == movies[1]:
    if hall_type == halls[0]:
        price = 7.35
    elif hall_type == halls[1]:
        price = 9.45
    elif hall_type == halls[2]:
        price = 12.75
elif title == movies[2]:
    if hall_type == halls[0]:
        price = 8.15
    elif hall_type == halls[1]:
        price = 10.25
    elif hall_type == halls[2]:
        price = 13.25
elif title == movies[3]:
    if hall_type == halls[0]:
        price = 8.75
    elif hall_type == halls[1]:
        price = 11.55
    elif hall_type == halls[2]:
        price = 13.95
revenue = n_tickets * price

print(f"{title} -> {revenue:.2f} lv.")
