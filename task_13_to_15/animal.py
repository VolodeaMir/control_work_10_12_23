import datetime

class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
        self.age = None
        self.commands = []

    def calculate_age(self):
        today = datetime.datetime.now()
        age = today - self.birth_date
        self.age = age.days // 365
        print(f"{self.name} возрастом {self.age} лет")

    def display_commands(self):
        print(f"{self.name} выполняет следующие команды: {', '.join(self.commands)}")

    def teach_command(self, new_command):
        self.commands.append(new_command)
        print(f"{self.name} теперь выполняет команду: {new_command}")

    def to_csv(self):
        return [self.name, self.birth_date.strftime('%Y-%m-%d'), ', '.join(self.commands)]

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.commands.append(command)

class Dog(DomesticAnimal):
    def __init__(self, name, birth_date, breed, command):
        super().__init__(name, birth_date, command)
        self.breed = breed

def create_animal():
    name = input("Введите имя животного: ")
    birth_date = input("Введите дату рождения животного (гггг-мм-дд): ")
    command = input("Введите команду, которую выполняет животное: ")

    return DomesticAnimal(name, birth_date, command)
