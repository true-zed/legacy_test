"""
A module with a duck class.
"""

from .animal import Animal


class Duck(Animal):
    """
    Duck class.
    """

    def __init__(self, name: str = 'Duck', init_parameters: dict = None):
        super().__init__(name=name, energy=100, init_parameters=init_parameters)

        if not self.energy_consumption:
            self.energy_consumption = {'swim': 10, 'fly': 30}
