from Animals import Animal


class Tiger(Animal):
    def __init__(self, name: str = 'Tiger', init_parameters: dict = None):

        super().__init__(name=name, energy=200,
                         init_parameters=init_parameters)

        if not self.energy_consumption:
            self.energy_consumption = {'run': 20, 'swim': 40}
