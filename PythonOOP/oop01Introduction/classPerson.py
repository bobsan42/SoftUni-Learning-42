class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f'{self.name} is eating..'


person = Person("Petar", 48)
print(person.eat())  # eating..
