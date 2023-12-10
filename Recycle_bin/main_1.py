import csv

class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1
        print(f"Значение счетчика увеличено. Текущее значение: {self.value}")

class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.age = None
        self.commands = []

    def calculate_age(self):
        # Логика расчета возраста
        pass

    def display_commands(self):
        print(f"{self.name} выполняет следующие команды: {', '.join(self.commands)}")

    def teach_command(self, new_command):
        self.commands.append(new_command)
        print(f"{self.name} теперь выполняет команду: {new_command}")

    def to_csv(self):
        return [self.name, self.birth_date, ', '.join(self.commands)]

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.commands.append(command)

class Dog(DomesticAnimal):
    def __init__(self, name, birth_date, breed, command):
        super().__init__(name, birth_date, command)
        self.breed = breed

# Пример использования

def create_animal():
    name = input("Введите имя животного: ")
    birth_date = input("Введите дату рождения животного (гггг-мм-дд): ")
    command = input("Введите команду, которую выполняет животное: ")

    return DomesticAnimal(name, birth_date, command)

def write_to_file(animal):
    with open('animal_registry.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(animal.to_csv())

def main():
    counter = Counter()

    while True:
        print("\nМеню:")
        print("1. Завести новое животное")
        print("2. Определить животное в правильный класс")
        print("3. Увидеть список команд животного")
        print("4. Обучить животное новым командам")
        print("5. Вывести все животные в реестре")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            new_animal = create_animal()
            write_to_file(new_animal)
            counter.add()

        elif choice == '2':
            # Логика определения класса животного
            pass

        elif choice == '3':
            # Логика вывода команд животного из файла
            pass

        elif choice == '4':
            # Логика обучения животного новой команде и запись в файл
            pass

        elif choice == '5':
            # Вывести все животные из файла
            with open('animal_registry.csv', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)

        elif choice == '6':
            break

        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()
