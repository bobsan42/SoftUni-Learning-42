class Person:
    text = 'hello'
    name = "George"
    age = 25

    def greet(self):
        return f'{self.name} says {self.text}.'


person = Person()
print(person.name)  # George
print(person.age)  # 25
print(person.greet())

class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []
