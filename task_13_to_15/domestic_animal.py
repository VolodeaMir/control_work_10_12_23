from animal import Animal

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.commands.append(command)
