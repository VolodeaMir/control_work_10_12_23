from domestic_animal import DomesticAnimal

class Dog(DomesticAnimal):
    def __init__(self, name, birth_date, breed, command):
        super().__init__(name, birth_date, command)
        self.breed = breed
