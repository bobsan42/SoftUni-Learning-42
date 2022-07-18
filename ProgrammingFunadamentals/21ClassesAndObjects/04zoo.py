class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if species == 'mammal':
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result = f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
a_count = int(input())

for _ in range(a_count):
    animal = input().split(' ')
    zoo.add_animal(animal[0], animal[1])

spec = input()
print(zoo.get_info(spec))
