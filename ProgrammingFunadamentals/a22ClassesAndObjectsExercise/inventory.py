class Inventory:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []

    def add_item(self, add_item: str):
        if len(self.items) < self.__capacity:
            
