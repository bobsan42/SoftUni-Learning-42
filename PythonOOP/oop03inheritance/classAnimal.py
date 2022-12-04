class Animal:
    def __init__(self):
        pass

    def eat(self):
        return 'eating...'

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        return 'barking...'

    def eat(self):
        return 'The dog is ' + super(Dog, self).eat()

dog = Dog()
print(dog.eat())
print(dog.bark())
