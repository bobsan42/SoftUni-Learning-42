class Validator:
    @staticmethod
    def raise_is_string_is_null_or_empty(value, errorMessage = 'Invalid string value provided'):
        if not value.strip():
            raise ValueError(errorMessage)


class Person:
    def __init__(self,name):
        self.name=name

    @property
    def name(self):
        return self.__name + ' altered'

    @name.setter
    def name(self,value):
        # if not value:
        #     raise ValueError('Invalid string value provided')
        Validator.raise_is_string_is_null_or_empty(value,'Error in class ' + self.__class__.__name__)
        self.__name = value

pp = Person('IME1')
print(pp.name)

class Animal:
    def __init__(self,name):
        self.name=name

    @property
    def name(self):
        return self.__name + ' Animal'

    @name.setter
    def name(self,value):
        Validator.raise_is_string_is_null_or_empty(value,'Error in class ' + self.__class__.__name__)
        # if not value.strip():
        #     raise ValueError('Invalid string value provided in class Animal')
        self.__name = value

an = Animal("    ")
print(an.name)