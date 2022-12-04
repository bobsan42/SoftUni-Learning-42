class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "parmesan", "pepperoni"])

    @classmethod
    def quattro_formaggi(cls):
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])

    def __str__(self):
        return ", ".join(self.ingredients)

first_pizza = Pizza.pepperoni()
second_pizza = Pizza.quattro_formaggi()
print(second_pizza)
print(first_pizza)