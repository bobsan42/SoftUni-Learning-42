class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def list_of_guests(self):
        return ', '.join([person.name for person in self.people])

    def number_of_guests(self):
        return len(self.people)


party = Party()
name = input()
while name != 'End':
    person = Person(name)
    party.invite(person)
    name = input()

print(f'Going: {party.list_of_guests()}')
print(f'Total: {party.number_of_guests()}')
