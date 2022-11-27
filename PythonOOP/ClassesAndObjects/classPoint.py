class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def __str__(self):
        return f'The point has coordinates ({self.x},{self.y})'

    def distance_to(self, point2):
        deltaX = self.x - point2.x
        deltaY = self.y-point2.y
        len = abs(deltaX ** 2 + deltaY**2)
        return len**.5


point = Point(2,4)
p2 = Point (3,5)
print(point.distance_to(p2))

p2.set_x(p2.x*2)
p2.set_y(p2.y*2)

print(point.distance_to(p2))