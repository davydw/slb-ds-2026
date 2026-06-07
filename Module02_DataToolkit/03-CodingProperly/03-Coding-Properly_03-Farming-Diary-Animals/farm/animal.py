# pylint: disable=too-few-public-methods
"""
This module defines the base `Animal` class, which serves as a parent class
for all animals in the farming diary application. It provides basic functionality
such as tracking energy and feeding behavior.
"""

class Animal:
    """
    A base class representing a generic animal.

    Attributes:
        energy (int): The energy level of the animal.
    """

    def __init__(self):
        """
        Initializes a new Animal instance with an energy level of 0.
        """
        self.energy = 0

    def feed(self):
        """
        Increases the animal's energy by 1.

        This method simulates feeding the animal, which boosts its energy.
        """
        self.energy += 1
