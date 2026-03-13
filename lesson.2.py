class Car:
    #Инициализатор(конструктор)
    def __init__(self, color, model ):
       self.color = color
       self.model = model

    def drive_to(self,destination):
        print(f"Машина:{self.model} едет в {destination}")

    def change_color(self, new_color):
        self.color = new_color

#Дочерний класс(Подкласс)
class Bus(Car):
    def __init__(self, color, model, seats_number ):
        super().__init__(color, model)
        self.seats_number = seats_number


    def drive_to(self,destination):
     super().drive_to(destination)
     print(f"Автобус:{self.model}  едет в {destination}. Мест в автобусе: {self.seats_number}")

class Truck(Car):
    def __init__(self, color, model, max_weight, seats_number):
        super().__init__(color, model)
        self.max_weight = max_weight
        self.seats_number = seats_number

    def drive_to(self,destination):
        print(f"Трак: {self.model} едет в {destination} \n Масса: {self.max_weight} \nМест в траке: {self.seats_number}")



car_ford = Car(color = 'Красный', model = '"Ford"')
bus = Bus(color="White",model=" Mercedes", seats_number=40)
print(bus.color,bus.model)
bus.drive_to('Бишкек')
truck =Truck(color="Black",model="Volkswagen", max_weight=50, seats_number=2)
truck.drive_to("Ош")
print(truck.model, truck.color,)

polik = [bus, truck ]
for v in polik:
    v.drive_to(destination="Kant")
    print(v.model, v.color)

