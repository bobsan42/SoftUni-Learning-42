class Party:
    def __init__(self):
        self.people = []


command = input()
guests = Party()
while command != 'End':
    guests.people.append(command)
    command = input()
people = ', '.join(guests.people)
print(f'Going: {people}')
print(f'Total: {len(guests.people)}')
