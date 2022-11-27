class Book:
    some_other_class_attribute = 'hello'
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
        self.published = False


book = Book('My Book', 'Me', 200)
book2 = Book('My Book 2', 'You', 250)

print(book2.name) # Attributes are public
book2.name= 'MB 3'
print(book2.name)
print(book2.some_other_class_attribute)
Book.some_other_class_attribute = 'NO'
print(book2.some_other_class_attribute)
print(book.some_other_class_attribute)
book2.some_other_class_attribute = 'YES'
print(book2.some_other_class_attribute)
print(book.some_other_class_attribute)
