class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.__is_full = False

    def add_product(self, product: str):
        if not self.__is_full:
            self.storage.append(product)
        if len(self.storage) == self.capacity:
            self.__is_full = True

    def get_products(self):
        return self.storage


# Test code

storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
