class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.age = None

    def calculate_age(self):
        # Логика расчета возраста
        pass

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.command = command

class Dog(DomesticAnimal):
    def __init__(self, name, birth_date, breed, command):
        super().__init__(name, birth_date, command)
        self.breed = breed

class Cat(DomesticAnimal):
    def __init__(self, name, birth_date, breed, command):
        super().__init__(name, birth_date, command)
        self.breed = breed



class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} добавлен в реестр.")
        else:
            print("Неверный тип животного.")

    def display_commands(self, animal):
        if isinstance(animal, DomesticAnimal):
            print(f"{animal.name} может выполнить следующие команды: {animal.command}")
        else:
            print("Это не домашнее животное.")

# Пример использования

registry = AnimalRegistry()

dog1 = Dog("Rex", "2020-01-01", "Labrador", "Sit")
cat1 = Cat("Murka", "2021-05-20", "Persian", "Meow")

registry.add_animal(dog1)
registry.add_animal(cat1)

registry.display_commands(dog1)
registry.display_commands(cat1)