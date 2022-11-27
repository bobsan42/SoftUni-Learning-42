class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        return f"{self.name} is sleeping.."

animal = Animal("cat")
print(animal.sleep()) # sleeping..


