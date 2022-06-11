n_seats = 0
n_kid = 0
n_student = 0
n_standard = 0
title = input()

while title != 'Finish':
    free_seats = int(input())
    seat_type = input()
    m_seats = 0
    while seat_type != 'End':  # T_ODO:  and m_seats <= free_seats:
        if m_seats == free_seats:
            break
        m_seats += 1
        if seat_type == 'kid':
            n_kid += 1
        elif seat_type == 'student':
            n_student += 1
        elif seat_type == 'standard':
            n_standard += 1
        if m_seats == free_seats:
            break
        seat_type = input()
    print(f"{title} - {(m_seats / free_seats * 100):.2f}% full.")
    title = input()

sold_tickets = n_kid + n_student + n_standard
print(f'Total tickets: {sold_tickets}')
print(f"{(n_student / sold_tickets * 100):.2f}% student tickets.")
print(f"{(n_standard / sold_tickets * 100):.2f}% standard tickets.")
print(f"{(n_kid / sold_tickets * 100):.2f}% kids tickets.")
