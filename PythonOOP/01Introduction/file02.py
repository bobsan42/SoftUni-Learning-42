class Phone:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def turn_on(self):
        return 'The phone is turned on'


phone = Phone('blue', 4.7)  # This creates an object of type Phone


class Person:
    def __init__(self, name, age):  # This creates an object
        self.name = name
        self.age = age


per = Person()
