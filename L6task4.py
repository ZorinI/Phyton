class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'{self.name}: текущая скорость {self.speed}'


class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.max_speed:
            return f'{self.name} превышение скорости!'
        else:
            return f'{self.name} - дозволительная скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'{self.name}: текущая скорость {self.speed}'

class WorkCar(TownCar):
    max_speed = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > self.max_speed:
            return f'{self.name} превышение скорости!'
        else:
            return f'{self.name} - дозволительная скорость'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'{self.name}: текущая скорость {self.speed}'


opel = TownCar(60, 'бирюзовый', 'Opel', False)
BMW = SportCar(130, 'черный', 'BMW', False)
reno = WorkCar(50, 'серый', 'reno', False)
lada = PoliceCar(80, 'голубой', 'Лада', True)
print(opel.show_speed())
print(reno.show_speed())
print(BMW.show_speed())
print(lada.show_speed())
print(f'Марка: {lada.name}, цвет: {lada.color}')
print(f'{lada.name} - Полиция? {lada.is_police}')
print(f'{BMW.name} - это Полиция? {BMW.is_police}')
print(f'{reno.turn_left()}, а {opel.turn_right()}')