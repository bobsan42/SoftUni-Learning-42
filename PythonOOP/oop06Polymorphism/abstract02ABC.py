from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod  # Makes a Method Abstract
    def perimeter(self):
        pass


# from abc import ABC, abstractmethod


class Animal(ABC): # Defining an Abstract Class
    def __init__(self, name):
        self.name = name

    @abstractmethod # Makes a Method Abstract
    def sound(self):
        raise NotImplementedError("Subclass must implement")


# Continues on next slide
class Dog(Animal):  # Inherit the Abstract Class
    def __init__(self, name):
        super().__init__(name)

    def sound(self):  # Implement the Abstract method
        print("Bark!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Meow!")


cat = Cat("Willy")
cat.sound()
dog = Dog("Willy")
dog.sound()
animal = Animal("Willy")
animal.sound()
# Meow!
# Bark!
# Error!