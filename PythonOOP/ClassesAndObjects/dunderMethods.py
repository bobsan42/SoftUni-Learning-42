class Dog:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def __str__(self):  # string representation of a class
        return 'This is Dog Class'

    def __repr__(self):
        return f'This is {self.name} Class'


x = Dog("Max")
print(x.__dict__)  # {"name": "Max"}
x = Dog("Max")
x.change_name("Rex")
print(x.name)  # Rex
print(x.__dict__)  # {"name": "Max"}
print(str(x))
print(x.__str__())
print(x)
print(repr(x))
print(x.__repr__())
print(x)             # This is My Class
# use print() only when __repr__() returns string

class MyClass:
    """This is MyClass."""

    def example(self):
        """This is the example module of MyClass."""

print(MyClass.__doc__) # This is MyClass.
print(MyClass.example.__doc__)
# This is the example module of MyClass.

class MyClass:
    class_variable = 1

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

first = MyClass(2)
second = MyClass(3)

print(MyClass.__dict__) # {'__module__': '__main__', ... }
print(first.__dict__)     # { 'instance_variable': 2 }
print(second.__dict__)    # { 'instance_variable': 3 }
