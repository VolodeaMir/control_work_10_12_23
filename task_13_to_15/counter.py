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
