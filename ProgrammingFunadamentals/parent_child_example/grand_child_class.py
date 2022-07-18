from ProgrammingFunadamentals.parent_child_example.child_class import Child


class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address


# Test code
test = GrandChild('Ivan Ivanov', 33, 'Gabrovo')
print(test.get_name(),'is', test.get_age(), 'years old and is from', test.get_address())
