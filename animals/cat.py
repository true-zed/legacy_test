"""
A module with a cat class.
"""
from .animal import Animal


class Cat(Animal):
    """
    Cat class.
    """

    def __init__(self, name: str = 'Cat', init_parameters: dict = None):
        super().__init__(name=name, energy=100, init_parameters=init_parameters)

        if not self.energy_consumption:
            self.energy_consumption = {'run': 5}
