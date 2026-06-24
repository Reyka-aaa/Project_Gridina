#Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров.
class Car:
    def __init__(self, b, m, y):
        self.b = b
        self.m = m
        self.y = y

    def info(self):
        print(f"Марка: {self.b}, Модель: {self.m}, Год: {self.y}")


class Truck(Car):
    def __init__(self, b, m, y, c):
        super().__init__(b, m, y)
        self.c = c

    def info(self):
        print(f"Марка: {self.b}, Модель: {self.m}, Год: {self.y}, Грузоподъемность: {self.c} т")


class PassengerCar(Car):
    def __init__(self, b, m, y, s):
        super().__init__(b, m, y)
        self.s = s

    def info(self):
        print(f"Марка: {self.b}, Модель: {self.m}, Год: {self.y}, Пассажиров: {self.s}")


c = Car("Toyota", "Camry", 2020)
t = Truck("Volvo", "FH16", 2019, 25)
p = PassengerCar("Honda", "Civic", 2021, 5)

c.info()
t.info()
p.info()
