n_kids = 0
n_students = 0
n_standard = 0
while True:
    title = input()
    if title == 'Finish':
        break
    seats = int(input())
    sold = 0
    while True:
        if seats - sold == 0:
            break
        x = input()
        if x == 'End':
            break
        sold += 1
        if x == 'kid':
            n_kids += 1
        elif x == 'student':
            n_students += 1
        elif x == 'standard':
            n_standard += 1

    print(f"{title} - {(sold / seats * 100):.2f}% full.")
sold = n_kids + n_students + n_standard

print(f"Total tickets: {sold}")
print(f"{(n_students / sold * 100):.2f}% student tickets.")
print(f"{(n_standard / sold * 100):.2f}% standard tickets.")
print(f"{(n_kids / sold * 100):.2f}% kids tickets.")
