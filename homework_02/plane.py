"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self,  weight=0, fuel=0, fuel_consumption=6, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo: int):
        if (self.cargo + cargo) <= self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        old_cargo_value = self.cargo
        self.cargo = 0
        return  old_cargo_value

