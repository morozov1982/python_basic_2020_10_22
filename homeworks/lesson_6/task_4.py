"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = 'green'
    name = 'машинка'
    is_police = False

    def __init__(self):
        print('На свет появилась новая машинка!')

    def go(self):
        print('Сообщаю, машина поехала!')

    def stop(self):
        print('Сообщаю, машина остановилась!')

    def turn(self, direction='up'):
        __directions = {"up": "вперёд", "down": "назад", "left": "налево", "right": "направо"}

        if direction in __directions:
            print(f'Машина движется {__directions[direction]}')
        else:
            raise Exception(f'Аттеншн: туда ваш(-а/-е) {self.name} не поедет!')

    def show_speed(self):
        print(f'Скорость: {self.speed}')

    def show_is_police(self):
        if self.is_police:
            print('Да, машинка полицейская!')
        else:
            print('Спокойно, это не полиция!')


class TownCar(Car):
    __max_speed = 60

    def __init__(self):
        print('Да здравствует общественный транспорт!')

    def show_speed(self):
        if self.speed > self.__max_speed:
            print(f'{self.speed} км/ч. Превышение скорости! Пассажиры в шоке!!!')
        else:
            print(f'Скорость: {self.speed}, не превышайте {self.__max_speed}')


class SportCar(Car):

    def __init__(self):
        print('Спорткар появился в городе!')


class WorkCar(Car):
    __max_speed = 40

    def __init__(self):
        print('Новая рабочая лошадка!')

    def show_speed(self):

        if self.speed > self.__max_speed:
            print(f'{self.speed} км/ч. Превышение скорости! Конец двигателю!!!')
        else:
            print(f'Скорость: {self.speed}, не превышайте {self.__max_speed}')


class PoliceCar(Car):

    def __init__(self):
        print('Полиция охраняет наш покой!')


if __name__ == '__main__':
    # Делаем просто машинку
    car = Car()

    car.show_speed()

    print('Цвет:', car.color)
    car.color = 'red'
    print('Цвет:', car.color)

    print('Название:', car.name)
    car.name = 'бибика'
    print('Название:', car.name)

    car.go()
    car.speed = 58
    car.show_speed()

    car.show_is_police()
    car.is_police = True
    car.show_is_police()

    car.turn('up')
    car.turn('left')
    car.turn('right')
    car.turn('down')
    car.turn('напрямо')
    car.stop()

    print('\n' + '*' * 25 + '\n')

    # TownCar
    town_car = TownCar()
    town_car.show_speed()
    town_car.go()
    town_car.speed = 42
    town_car.show_speed()
    town_car.speed = 128
    town_car.show_speed()
    town_car.stop()

    print('\n' + '*' * 25 + '\n')

    # SportCar
    sport_car = SportCar()
    print('Пусть эта красивая машинка просто постоит в гараже!')

    print('\n' + '*' * 25 + '\n')

    # WorkCar
    work_car = WorkCar()
    work_car.show_speed()
    work_car.go()
    work_car.speed = 35
    work_car.show_speed()
    work_car.speed = 41
    work_car.show_speed()
    work_car.stop()

    print('\n' + '*' * 25 + '\n')

    # PoliceCar
    police_car = PoliceCar()
    print('Теперь в городе будет порядок и никто не превысит скорость!')

    print('\n' + '*' * 25 + '\n')
    print('Достаточно проверок!')
    print('\n' + '*' * 25 + '\n')
