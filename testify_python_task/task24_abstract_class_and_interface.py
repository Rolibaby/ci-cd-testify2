# create an Abstract class called Vehicle
import abc


class Vehicle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def drive_direction(self):  # create an abstract method called drive_direction()
        pass


class Car(Vehicle):  # create another class Car that inherits from Vehicle
    def drive_direction(self):
        return "Car: drive Forward"


class Plane(Vehicle):  # create another class Plane that inherits from Vehicle
    def drive_direction(self):
        return "Plane: Fly Upward"


car = Car()
print(car.drive_direction())
plane = Plane()
print(plane.drive_direction())
