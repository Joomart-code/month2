class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Возраст должен быть положительным числом")

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return f"{self.get_name()} говорит: Гав гав"

class Cat(Animal):
    def make_sound(self):
        return f"{self.get_name()} говорит: Мяу"


if __name__ == "__main__":
    doggy = Dog("Бобик", 5)
    kitty = Cat("Мурка", 3)

    animals = [doggy, kitty]
    print("Звуки животных:")
    for animal in animals:
        print(animal.make_sound())

    print("\nИзменение данных через сеттеры:")

    print(f"Старый возраст {kitty.get_name()}: {kitty.get_age()}")

    kitty.set_age(2)
    kitty.set_name("Луна")

    print(f"Новое имя: {kitty.get_name()}")
    print(f"Новый возраст: {kitty.get_age()}")
    doggy.set_age(-5)