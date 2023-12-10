from counter import Counter
from animal_registry import AnimalRegistry
from animal import Animal, DomesticAnimal, Dog, create_animal

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
