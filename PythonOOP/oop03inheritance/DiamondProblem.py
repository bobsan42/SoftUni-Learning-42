class Parent:
    pass

class FirstChild(Parent):
    pass

class SecondChild(Parent):
    pass

class GrandChild(SecondChild, FirstChild):
    pass
# Methods Resolution Order
print(GrandChild.mro())
# [<class '__main__.GrandChild'>, <class '__main__.SecondChild'>, <class '__main__.FirstChild'>, <class '__main__.Parent'>, <class 'object'>]
