class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name)
        print(self.__age)

    def get_age(self):       # getter
        print(self.__age)

    def set_age(self, age):  # setter
        self.__age = age

person = Person('Peter', 25)

# accessing data using class method
person.info()	# Peter
		# 25

# changing age using setter
person.set_age(26)
person.get_age()	# 26
