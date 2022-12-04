class Parent:
  def say_hi(self):
      return "Hello!"

class Child(Parent):
    def go_school(self):
       return "I go to school."

child = Child()
print(child.say_hi())    # Hello!
print(child.go_school()) # I go to school.
