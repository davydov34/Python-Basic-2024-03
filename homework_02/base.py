from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 2
    started: bool = False
    fuel: int = 75
    fuel_consumption: int = 3

    def __init__(self, weight=0, fuel=0, fuel_consumption=6):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started != True:
            if self.fuel == 0:
                raise LowFuelError
            else:
                self.started = True

    def move(self, distance):
        max_distance = self.fuel / self.fuel_consumption
        if distance <= max_distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel
