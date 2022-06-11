sector_last = input()
sector_first = 'A'
ascii_capital_a = ord(sector_first)
ascii_small_a = ord('a')
n_rows_sector_A = int(input())
odd_row_seats = int(input())
count_seats = 0
for s in range(ord(sector_first), ord(sector_last) + 1):  # loop sectors
    rows_in_sector = n_rows_sector_A + (s - ascii_capital_a)
    for r in range(1, rows_in_sector + 1):
        # if r % 2 == 1:
        #     seats_in_row = odd_row_seats
        # else:
        #     seats_in_row = odd_row_seats+2
        seats_in_row = odd_row_seats + 2 * (r % 2 == 0)
        for seat in range(seats_in_row):
            print(f'{chr(s)}{r}{chr(ascii_small_a+ seat)}')
            count_seats +=1

print(count_seats)