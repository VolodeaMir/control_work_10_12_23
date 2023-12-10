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

class Hamster(DomesticAnimal):
    def __init__(self, name, birth_date, color, command):
        super().__init__(name, birth_date, command)
        self.color = color

class WorkingAnimal(Animal):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.command = command

class Horse(WorkingAnimal):
    def __init__(self, name, birth_date, color, command):
        super().__init__(name, birth_date, command)
        self.color = color

class Camel(WorkingAnimal):
    def __init__(self, name, birth_date, color, command):
        super().__init__(name, birth_date, command)
        self.color = color

class Donkey(WorkingAnimal):
    def __init__(self, name, birth_date, color, command):
        super().__init__(name, birth_date, command)
        self.color = color