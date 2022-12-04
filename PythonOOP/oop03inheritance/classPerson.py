class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):  # Subclassing
    pass


# An Object of class Student
student = Student("John", "Smith")
print(student.get_full_name())
# John Smith
