class Person:
    def __init__(self, name, birth_date, job):
        self.name = name
        self.birth_date = birth_date
        self.job = job

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, работаю {self.job}")


class Classmate(Person):
    def __init__(self, name, birth_date, job, group_name):
        super().__init__(name, birth_date, job)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одногруппник из группы {self.group_name}, "
              f"я родился {self.birth_date}, работаю {self.job}")


class Friend(Person):
    def __init__(self, name, birth_date, job, hobby):
        super().__init__(name, birth_date, job)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг, я родился {self.birth_date}, "
              f"работаю {self.job}, мое хобби — {self.hobby}")



classmate1 = Classmate("Бектур", "05.12.2000", "программист", "geeks 64-1")
classmate2 = Classmate("Нурлан", "12.03.2001", "дизайнер", "geeks 64-1")


friend1 = Friend("Алмаз", "10.08.2000", "разработчик", "футбол")
friend2 = Friend("Тимур", "21.11.1999", "маркетолог", "игры")


classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()