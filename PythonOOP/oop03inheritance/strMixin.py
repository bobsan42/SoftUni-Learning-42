class StrMixin():
    def __str__(self):
        items = self.__dict__.items()
        return ';'.join([f'{key}={value}' for key, value in items])

    def sleep(object):
        # return object.name + ' is sleeping'
        try:
            return object.name + ' is sleeping'
        except:
            pass


class Animal(StrMixin):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Vet(StrMixin):
    def __init__(self, location, name):
        self.location = location
        self.names = name


a = Animal('Yuki', 'male', 2)
v = Vet('ul. Kokiche 14', 'dr. Shterev')
print(str(a))
print(str(v))
print(a.sleep())
print(v.sleep())