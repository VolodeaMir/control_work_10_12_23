import csv
import datetime

class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1
        print(f"Значение счетчика увеличено. Текущее значение: {self.value}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("Произошла ошибка. Ресурс не закрыт.")
            return False
        else:
            print("Ресурс успешно закрыт.")
            return True

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

def create_animal():
    name = input("Введите имя животного: ")
    birth_date = input("Введите дату рождения животного (гггг-мм-дд): ")
    command = input("Введите команду, которую выполняет животное: ")

    return DomesticAnimal(name, birth_date, command)

def main():
    with Counter() as counter:
        animal_registry = AnimalRegistry()

        while True:
            print("\nМеню:")
            print("1. Завести новое животное")
            print("2. Определить животное в правильный класс")
            print("3. Увидеть список команд животного")
            print("4. Обучить животное новым командам")
            print("5. Вывести всех животных в реестре")
            print("6. Выход")

            choice = input("Выберите действие (1-6): ")

            if choice == '1':
                counter.add()
                new_animal = create_animal()
                animal_registry.add_animal(new_animal)

            elif choice == '2':
                animal_name = input("Введите имя животного: ")
                animal = animal_registry.find_animal(animal_name)
                if animal:
                    print(f"{animal_name} принадлежит классу {animal.__class__.__name__}")
                else:
                    print("Животное не найдено.")

            elif choice == '3':
                animal_name = input("Введите имя животного: ")
                animal = animal_registry.find_animal(animal_name)
                if animal:
                    animal.display_commands()
                else:
                    print("Животное не найдено.")

            elif choice == '4':
                animal_name = input("Введите имя животного: ")
                animal = animal_registry.find_animal(animal_name)
                if animal:
                    new_command = input("Введите новую команду: ")
                    animal.teach_command(new_command)
                else:
                    print("Животное не найдено.")

            elif choice == '5':
                animal_registry.display_all_animals()

            elif choice == '6':
                break

            else:
                print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()
