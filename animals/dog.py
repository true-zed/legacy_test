"""
A module with a dog class.
"""

from .animal import Animal


class Dog(Animal):
    """
    Dog class.
    """

    def __init__(self, name: str = 'Dog', init_parameters: dict = None):
        super().__init__(name=name, energy=100, init_parameters=init_parameters)

        if not self.energy_consumption:
            self.energy_consumption = {'run': 10, 'swim': 30}
