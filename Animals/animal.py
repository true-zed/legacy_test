class Animal:
    def __init__(self,
                 name: str = 'Animal',
                 energy: int = 100,
                 init_parameters: dict = None,
                 energy_consumption: dict = None,
                 text_templates: dict = None):

        if init_parameters is None:
            init_parameters = {}

        self.name = init_parameters.get('name') or name
        self.energy = init_parameters.get('energy') or energy

        self.energy_consumption = init_parameters.get('energy_consumption',
                                                      energy_consumption or {})

        self._templates = init_parameters.get('text_templates',
                                              text_templates or
                                              self.__get_std_text_templates())

    def say(self):
        print(f"Hello, I'm {self.__class__.__name__} and "
              f"my name is {self.name}.")

    def run(self):
        self._do_action(action='run', print_text=True)

    def swim(self):
        self._do_action(action='swim', print_text=True)

    def fly(self):
        self._do_action(action='fly', print_text=True)

    def get_energy(self):
        return self.energy

    def _do_action(self, action: str, print_text=False) -> bool:
        if action not in self._templates.keys():
            if print_text:
                print(f"My name is {self.name} and "
                      f"I don't know what is \"{action}\".")
            return False

        energy_consumption = self.energy_consumption.get(action, 0)
        self.energy -= energy_consumption

        if print_text:
            text = self._templates[action]['t' if energy_consumption else 'f']
            print(f"My name is {self.name} and I {text}")

        return bool(energy_consumption)

    @staticmethod
    def __get_std_text_templates():
        return {"run": {"t": "running.", "f": "can't run."},
                "swim": {"t": "swimming.", "f": "can't swim."},
                "fly": {"t": "flying.", "f": "can't fly."}}
