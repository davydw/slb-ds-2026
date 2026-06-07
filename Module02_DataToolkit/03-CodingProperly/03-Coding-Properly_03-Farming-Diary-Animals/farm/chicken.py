"""
This module defines the `Chicken` class, which represents a chicken in the farming diary
application.
The `Chicken` class inherits from the `Animal` class and adds specific behavior such as laying eggs
and making gender-specific sounds.
"""

from farm.animal import Animal

class Chicken(Animal):
    """
    A class representing a chicken, inheriting from the `Animal` class.

    Attributes:
        gender (str): The gender of the chicken, either "male" or "female".
        eggs (int): The number of eggs laid by the chicken (only for females).
    """

    def __init__(self, gender):
        """
        Initializes a new Chicken instance with a specified gender.

        Args:
            gender (str): The gender of the chicken, either "male" or "female".
        """
        super().__init__()
        self.gender = gender
        self.eggs = 0

    def feed(self):
        """
        Increases the chicken's energy by 1 and adds 2 eggs if the chicken is female.

        This method overrides the `feed` method from the `Animal` class.
        """
        super().feed()
        if self.gender == "female":
            self.eggs += 2

    def talk(self):
        """
        Returns the sound made by the chicken based on its gender.

        Returns:
            str: "cock-a-doodle-doo" if the chicken is male, "cluck cluck" if female.
        """
        if self.gender == "male":
            return "cock-a-doodle-doo"
        if self.gender == "female":
            return "cluck cluck"
        raise ValueError("Unknown gender")
