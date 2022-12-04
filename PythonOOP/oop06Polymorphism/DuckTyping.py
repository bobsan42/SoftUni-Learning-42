class Cat:
    def sound(self):
        print("Meow!")


class Train:
    def sound(self):
        print("Sound from wheels slipping!")


for any_type in Cat(), Train():
    any_type.sound()


######################

# Test Code
class Guitar:
    def play(self):
        return "Playing the guitar"


# Test Code
class Children:
    def play(self):
        return "Children are playing"


def start_playing(obj):
    try:
        print(obj.play())
        # obj.play()
    except:
        pass


piano = Children()
start_playing(piano)
# Children are playing

guitar = Guitar()
start_playing(guitar)
# Playing the guitar
