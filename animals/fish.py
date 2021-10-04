"""
A module with a fish class.
"""

from .animal import Animal


class Fish(Animal):
    """
    Fish class.
    """

    def __init__(self, name: str = 'Fish', init_parameters: dict = None):

        super().__init__(name=name, energy=100, init_parameters=init_parameters)

        if not self.energy_consumption:
            self.energy_consumption = {'swim': 5}


class FlyingFish(Animal):
    """
    Flying fish class.
    """

    def __init__(self, name: str = 'FlyingFish', init_parameters: dict = None):

        super().__init__(name=name, energy=100, init_parameters=init_parameters)

        if not self.energy_consumption:
            self.energy_consumption = {'swim': 5, 'fly': 20}
