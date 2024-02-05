'''
Some classes require a lot of steps to create/initialize a object
and can be initialized in a lot of ways.
One solution is to create a huge constructor and initialize everything.
But sometimes we don't need all the parts of the initializaton for all the objects,

Suppose we are creating a house object, some houses may have a pool, some have a lawn,
but all houses will not have that. So we use builder pattern for this situation.

Builder patterns gives apis to initialize the objects in steps by calling the apis.
'''

from abc import ABC, abstractmethod


class Car:
    def __init__(self, seats: int, gears: int, gps_device, automatic = False) -> None:
        self.seats = seats
        if(self.seats > 5):
            self.car_type = "SUV"
        if not automatic:
            self.gears = gears
            self.clutch = True
        self.gps_device = gps_device

'''
In the above class there are so many steps in the constructor.
Let's use builder patter to do this.
'''
class CarNew:
    def __init__(self) -> None:
        self.seats = 0
        self.car_type: str | None = None
        self.gears = 0
        self.clutch = False
        self.gps_device: str | None = None

class ICarBuilder(ABC):
    @abstractmethod
    def build_seats(self, seats: int) -> None:
        pass
    
    @abstractmethod
    def build_gps(self, gps_device) -> None:
        pass

    @abstractmethod
    def build_gears(self, gears: int) -> None:
        pass

    @abstractmethod
    def get_car(self) -> CarNew:
        pass


class CarBuilder(ICarBuilder):
    def __init__(self) -> None:
        self.car = CarNew()

    def build_seats(self, seats: int) -> None:
        self.car.seats = seats
        if(seats > 5):
            self.car.car_type = "SUV"
    
    def build_gps(self, gps_device) -> None:
        self.car.gps_device = gps_device

    def build_gears(self, gears: int) -> None:
        self.car.gears = gears
        self.car.clutch = True

    def get_car(self) -> CarNew:
        return self.car


''' 
You can go further and extract a series of calls to the builder
steps you use to construct a product into a separate class called director.
The director class defines the order in which to execute the building steps, 
while the builder provides the implementation for those steps.

Having a director class in your program isn't strictly necessary. 
You can always call the building steps in a specific order directly 
from the client code. However, the director class might be a good place to 
put various construction routines so you can reuse them across your program.
'''

class Director:
    def __init__(self, builder: ICarBuilder) -> None:
        self.builder = builder

    def build_auto_suv_with_gps(self) -> CarNew:
        self.builder.build_seats(7)
        self.builder.build_gps("high_end_gps_device")
        return self.builder.get_car()
    
    def build_manual_sedan(self) -> CarNew:
        self.builder.build_gps(7)
        self.builder.build_gears(5)
        return self.builder.get_car()