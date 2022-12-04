from classPerson import Person

class Student3 (Person):
    pass

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} is {self.age} years old.'

class Student2(Person2):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id

# Create an object of the superclass
person = Person2("John", 25)
print(person.get_info())
# returns 'John is 25 years old.'

# Create an object of the subclass
student = Student2("Leo", 20, 10035464)
print(student.get_info())
# returns 'Leo is 20 years old.'
print(student.get_id())
# returns 10035464
student3= Student3 ('Georgi','Petrov')
print(student3.get_full_name() + ' - imported subclass')