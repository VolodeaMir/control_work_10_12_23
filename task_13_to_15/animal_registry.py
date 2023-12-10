class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def find_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None

    def display_all_animals(self):
        for animal in self.animals:
            print(f"{animal.name} ({animal.__class__.__name__})")
