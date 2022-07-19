class Catalogue:
    # TODO : JUDGE 75/100

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):  # - adds the product to the products list
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        # - returns a list containing only the products that start with the given letter
        # return [item for item in self.products if item[0].lower() == first_letter.lower()]
        return [item for item in self.products if item[0] == first_letter]

    def __repr__(self):  # returns the catalogue info in the following format:
        # "Items in the {name} catalogue:
        # {item1}
        # {item2}
        # …
        # {itemN}
        # "
        # The items should be sorted alphabetically in ascending order.
        result = f'Items in the {self.name} catalogue:\n'
        for item in sorted(self.products):
            result += f'{item}\n'
        return result


# Test code
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
