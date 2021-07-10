class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Новая машина: скорость {self.speed}, {self.name} цвет: {self.color}, машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала")

    def stop(self):
       print(f"{self.name}: Машина остановилась")

    def turn_right(self):
        print(f"{self.name}: Машина повернула направо")

    def turn_left(self):
        print(f"{self.name}: Машина повернула налево")

    def show_speed(self):
        print(f"{self.name}: Скорость: {self.speed} ")


class TownCar(Car):
    '''Городской автомобиль'''

    def show_speed(self):
        if self.speed > 40:
            return f"{self.name} Превышение скорости"
        else:
            return f"{self.name} Нормальная скорость"

class SportCar(Car):
    '''Спортивный автомобиль'''


class WorkCar(Car):
    '''Рабочий автомобиль'''

    def show_speed(self):
        if self.speed > 40:
            return f"{self.name} Превышение скорости"
        else:
            return f"{self.name} Нормальная скорость"


class PoliceCar(Car):
    '''Полицейский автомобиль'''

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


audi = SportCar(100, "Красный", "Audi")
audi.go()
print(audi.show_speed())
audi.turn_right()
audi.stop()


oka = TownCar(30, "White", "Oka")
oka.go()
print(oka.show_speed())
oka.turn_right()
oka.stop()


lada = WorkCar(70, "Rose", "Lada")
lada.go()
print(lada.show_speed())
lada.turn_right()
lada.stop()

ford = PoliceCar(110, "Blue", "Ford", True)
ford.go()
print(ford.show_speed())
ford.turn_right()
ford.stop()
