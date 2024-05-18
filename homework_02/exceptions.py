"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    print('ERROR: Fuel has low lever')


class NotEnoughFuel(Exception):
    print('Fuel is not enough for this length route.')

class CargoOverload(Exception):
    print('This cargo is over hard.')
