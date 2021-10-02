"""
Tests for other animal classes.

Here are tests for checking the predefined values of the Animal child classes.
"""

import pytest

from Animals import Cat, Dog, Fish, FlyingFish, Tiger, Duck


test_cat = Cat()
test_dog = Dog()
test_fish = Fish()
test_flying_fish = FlyingFish()
test_tiger = Tiger()
test_duck = Duck()

name_test = [
    (test_cat, 'Cat'), (test_dog, 'Dog'),
    (test_fish, 'Fish'), (test_tiger, 'Tiger'),
    (test_flying_fish, 'FlyingFish'), (test_duck, 'Duck')]

energy_test = [
    (test_cat, 100), (test_dog, 100),
    (test_fish, 100), (test_tiger, 200),
    (test_flying_fish, 100), (test_duck, 100)]

actions_test = [
    (test_cat, 'run', True), (test_dog, 'run', True),
    (test_fish, 'run', False), (test_flying_fish, 'run', False),
    (test_tiger, 'run', True), (test_duck, 'run', False),
    (test_cat, 'swim', False), (test_dog, 'swim', True),
    (test_fish, 'swim', True), (test_flying_fish, 'swim', True),
    (test_tiger, 'swim', True), (test_duck, 'swim', True),
    (test_cat, 'fly', False), (test_dog, 'fly', False),
    (test_fish, 'fly', False), (test_flying_fish, 'fly', True),
    (test_tiger, 'fly', False), (test_duck, 'fly', True)
]

actions_energy_test = [
    (test_cat, 'run', 5), (test_dog, 'run', 10),
    (test_fish, 'run', 0), (test_flying_fish, 'run', 0),
    (test_tiger, 'run', 20), (test_duck, 'run', 0),
    (test_cat, 'swim', 0), (test_dog, 'swim', 30),
    (test_fish, 'swim', 5), (test_flying_fish, 'swim', 5),
    (test_tiger, 'swim', 40), (test_duck, 'swim', 10),
    (test_cat, 'fly', 0), (test_dog, 'fly', 0),
    (test_fish, 'fly', 0), (test_flying_fish, 'fly', 20),
    (test_tiger, 'fly', 0), (test_duck, 'fly', 30),
]


@pytest.mark.parametrize('animal, expected', name_test)
def test_animals_name(animal, expected):
    """
    Basic test to confirm that the name is set (predefined) correctly.

    :param animal: Class of testing animal.
    :param expected: Expected (predefined) name.
    """
    assert animal.name == expected


@pytest.mark.parametrize('animal, expected', energy_test)
def test_animals_energy(animal, expected):
    """
    Basic test to confirm that the energy is set (predefined) correctly.

    :param animal: Class of testing animal.
    :param expected: Expected (predefined) energy level.
    """
    assert animal.energy == expected


@pytest.mark.parametrize(('animal', 'action', 'expected'), actions_test)
def test_animals_actions(animal, action, expected):
    """
    Basic test to confirm that the action is set (predefined) correctly.

    :param animal: Class of testing animal.
    :param action: Animals actions like 'say', 'run'.
    :param expected: A pool of expected (predefined) actions.
    """
    assert animal._do_action(action=action) == expected  # pylint: disable=W0212


@pytest.mark.parametrize(('animal', 'action', 'expected'), actions_energy_test)
def test_animals_actions_energy_consumption(animal, action, expected):
    """
    Basic test to confirm that the action consumption is set (predefined) correctly.

    :param animal: Class of testing animal.
    :param action: Animals actions like 'say', 'run'.
    :param expected: Expected (predefined) energy consumption.
    """
    start_energy = animal.get_energy()
    animal._do_action(action=action)  # pylint: disable=W0212
    assert start_energy - animal.get_energy() == expected
