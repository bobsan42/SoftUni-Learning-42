class Shape:
    def __init__(self):
        if type(self) == Shape:
            raise Exception('…')
    def area(self):
        raise Exception('…')
    def perimeter(self):
        raise Exception('…')
