"""
This module defines the `Cow` class, which represents a cow in the farming diary application.
The `Cow` class inherits from the `Animal` class and adds specific behavior such as producing milk
and making a characteristic sound.
"""

from farm.animal import Animal

class Cow(Animal):
    """
    A class representing a cow, inheriting from the `Animal` class.

    Attributes:
        milk (int): The amount of milk produced by the cow.
    """

    def __init__(self):
        """
        Initializes a new Cow instance with an initial milk production of 0.
        """
        super().__init__()
        self.milk = 0

    def feed(self):
        """
        Increases the cow's energy by 1 and adds 2 liters of milk.

        This method overrides the `feed` method from the `Animal` class.
        """
        super().feed()
        self.milk += 2

    def talk(self):
        """
        Returns the sound made by the cow.

        Returns:
            str: The sound "moo".
        """
        return "moo"
