"""
Tests for Animal class.

Here are the tests to test the main logic of the base Animal class.
"""

from contextlib import redirect_stdout

import io
import pytest

from animals.animal import Animal


STD_ANIMAL_NAME = 'standard animal'
std_energy_consumption = {"run": 5, "swim": 5, "fly": 5}

can_action_templates = {
    "say": f"Hello, I'm Animal and my name is {STD_ANIMAL_NAME}.",
    "run": f"My name is {STD_ANIMAL_NAME} and I running.",
    "swim": f"My name is {STD_ANIMAL_NAME} and I swimming.",
    "fly": f"My name is {STD_ANIMAL_NAME} and I flying."
}
cant_action_templates = {
    "say": f"Hello, I'm Animal and my name is {STD_ANIMAL_NAME}.",
    "run": f"My name is {STD_ANIMAL_NAME} and I can't run.",
    "swim": f"My name is {STD_ANIMAL_NAME} and I can't swim.",
    "fly": f"My name is {STD_ANIMAL_NAME} and I can't fly."
}

templates = list(can_action_templates.items()) + list(cant_action_templates.items())

unknown_action_answer = f"My name is {STD_ANIMAL_NAME} and I don't know what is \"unknown_action\"."
init_params_list = [
    {},
    {'name': 'test_animal'},
    {'energy': 300},
    {'energy_consumption': std_energy_consumption},
    {'templates': {}},
    {'name': 'test_animal_full', 'energy': 250,
     'energy_consumption': std_energy_consumption,
     'templates': {"some_template": "test"}},
    {'name': 'test_animal_wo_tmp', 'energy': 200,
     'energy_consumption': std_energy_consumption},
    {'name': 'test_animal_wo_tmp_ec', 'energy': 150}
]


@pytest.fixture
def animal_for_test():
    """
    Fixture for creating test animal class.

    :return: Base animal for tests.
    """
    return Animal(name=STD_ANIMAL_NAME, energy_consumption=std_energy_consumption)


def test_animal_create(animal_for_test):  # pylint: disable=W0621
    """
    Basic test to confirm the creation of the class without errors.

    :param animal_for_test: Class of testing animal.
    """
    assert isinstance(animal_for_test, Animal)


def test_animal_name(animal_for_test):  # pylint: disable=W0621
    """
    Basic test to confirm that the name is set correctly.

    :param animal_for_test: Class of testing animal.
    """
    assert animal_for_test.name == STD_ANIMAL_NAME


def test_animal_energy_exist(animal_for_test):  # pylint: disable=W0621
    """
    Basic test to confirm that the energy is set correctly and exists.

    :param animal_for_test: Class of testing animal.
    """
    assert animal_for_test.energy


@pytest.mark.parametrize(('action', 'expected'), templates)
def test_animal_speak(animal_for_test, action, expected):  # pylint: disable=W0621
    """
    Basic test for comparing the speech of an animal in action with a template.

    :param animal_for_test: Class of testing animal.
    :param action: animals actions like 'say', 'run'.
    :param expected: Expected speech in action.
    """
    if "can't" in expected:
        animal_for_test.energy_consumption = {}

    say = io.StringIO()
    with redirect_stdout(say):
        animal_for_test.__getattribute__(action).__call__()

    assert say.getvalue().strip() == expected


def test_animal_unknown_action(animal_for_test):  # pylint: disable=W0621
    """
    Test for comparing the speech of an animal in unknown action with a template.

    :param animal_for_test: Class of testing animal.
    """
    say = io.StringIO()
    with redirect_stdout(say):
        animal_for_test._do_action(action='unknown_action', print_text=True)  # pylint: disable=W0212

    assert say.getvalue().strip() == unknown_action_answer


@pytest.mark.parametrize('action', ['run', 'swim', 'fly'])
def test_animal_action_energy(animal_for_test, action):  # pylint: disable=W0621
    """
    Basic test for comparing the energy consumption of an animal with a template.

    :param animal_for_test: Class of testing animal.
    :param action: animals actions like 'say', 'run'.
    """
    start_energy = animal_for_test.get_energy()

    with redirect_stdout(None):
        animal_for_test.__getattribute__(action).__call__()

    end_energy = animal_for_test.get_energy()

    assert start_energy - end_energy == animal_for_test.energy_consumption[action]


@pytest.mark.parametrize('init_params', init_params_list)
def test_animal_init_parameters(init_params):
    """
    Test for checking the functionality of the initial parameters.

    :param init_params: Initial parameters for check.
    """
    animal = Animal(init_parameters=init_params)

    assert all(
        (animal.name == init_params.get('name', 'Animal'),
         animal.energy == init_params.get('energy', 100),
         animal.energy_consumption == init_params.get('energy_consumption', {}),
         animal._templates == init_params.get('text_templates', animal._templates))  # pylint: disable=W0212
    )
