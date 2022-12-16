class Vehicle:

    def __init__(self, position):  # position: кортеж (10, 20)
        self.position = position

    def __str__(self):
        return str(self.position)

    def travel(self, destination):
        route = self.calculate_route(source=self.position, to=destination)
        self.move_along(route)

    @staticmethod
    def calculate_route(source, to):
        return 0  # to be realized

    def move_along(self, route):
        print("moving")

class MixRadio:

    def turn_on_radio(self, station=None):
        return f"Playing {station}"


class Car(Vehicle, MixRadio):
    pass
    # def __init__(self, position):
    #     super().__init__(position)
    #     super().turn_on_radio()


class Airplane(Vehicle):
    pass

if __name__ == "__main__":
    car = Car((10, 20))
    print(car)
    print(car.turn_on_radio('Moscow FM'))

