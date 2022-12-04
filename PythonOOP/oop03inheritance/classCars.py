class Vehicle():
    def move(self):
        return 'moving...'

class Car(Vehicle):
    def drive(self):
        return 'driving...'

class SportsCar(Car):
    def race(self):
        return 'racing...'