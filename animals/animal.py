"""
A module with the base class of the animal.
"""


class Animal:
    """
    Base class for creating an animal.
    """

    __std_text_templates = {"run": {"t": "running.", "f": "can't run."},
                            "swim": {"t": "swimming.", "f": "can't swim."},
                            "fly": {"t": "flying.", "f": "can't fly."}}

    def __init__(self,
                 name: str = 'Animal',
                 energy: int = 100,
                 init_parameters: dict = None,
                 energy_consumption: dict = None):
        """
        Animal initial.

        :param name: Animal name.
        :param energy: Animal energy level.
        :param init_parameters: Initial parameters.
        :param energy_consumption: Possible actions and energy consumption for them.
        """

        if init_parameters is None:
            init_parameters = {}

        self.name = init_parameters.get('name', name)
        self.energy = init_parameters.get('energy', energy)

        self.energy_consumption = init_parameters.get('energy_consumption', energy_consumption or {})
        self._templates = init_parameters.get('text_templates', self.__std_text_templates)

    def say(self) -> bool:
        """
        Method for making the animal speak.
        """

        print(f"Hello, I'm {self.__class__.__name__} and my name is {self.name}.")
        return True

    def run(self) -> bool:
        """
        Method for making the animal run.
        """

        return self._do_action(action='run', print_text=True)

    def swim(self) -> bool:
        """
        Method for making the animal swim.
        """

        return self._do_action(action='swim', print_text=True)

    def fly(self) -> bool:
        """
        Method for making the animal fly.
        """

        return self._do_action(action='fly', print_text=True)

    def get_energy(self) -> int:
        """
        Method for getting the energy level of an animal.
        """

        return self.energy

    def _do_action(self, action: str, print_text: bool = False) -> bool:
        """
        Protected method for making the animal action.
        :param action: Action text name.
        :param print_text: Outputting a replica to action.
        :return: True if the action was, otherwise False.
        """

        if action not in self._templates.keys():
            if print_text:
                print(f"My name is {self.name} and I don't know what is \"{action}\".")
            return False

        energy_consumption = self.energy_consumption.get(action, 0)
        self.energy -= energy_consumption

        if print_text:
            text = self._templates[action]['t' if energy_consumption else 'f']
            print(f"My name is {self.name} and I {text}")

        return bool(energy_consumption)
