class Laptop:
    brand = "Dell"            # class variable

    def __init__(self, name):
        self.name = name      # instance variable

first_laptop = Laptop("Latitude 5300")
second_laptop = Laptop("Inspiron 15")
print(first_laptop.brand == second_laptop.brand)  # True
print(first_laptop.name == second_laptop.name)   # False
