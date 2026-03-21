class Car:
    #Инициализатор(конструктор)
    def __init__(self, color, model ):
       self.color = color
       self.model = model

    def drive_to(self,destination):
        print(f"Машина: {self.model} едет в {destination}")

    def change_color(self, new_color):
        self.color = new_color

    def shtraf(self, prev):
        if car1.color or car2.color == "черный":
            print(f"Машинам цвета {prev} запрещен проезд  ")


car1 = Car(color = 'Красный', model = '"Ford"')
car2 = Car(color = 'Синий', model = '"Porche"')
print(f"Цвет первой машины: {car1.color}.\nМодель: {car1.model}")
print(f"Цвет второй машины: {car2.color}.\nМодель: {car2.model}. ")
car1.drive_to("Бишкек")
car2.drive_to("Каракол")
car1.change_color(new_color="черный")
print(f'Цвет машины {car1.model} теперь "{car1.color}"')
car1.shtraf(prev="'Черный'")