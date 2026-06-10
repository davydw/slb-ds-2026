# $DELETE_BEGIN
# pylint: disable=pointless-string-statement
"""
Module: corn
This module contains the Corn class, which is a subclass of Crop. It represents a specific type of
crop and provides a method for watering the corn to increase its grains.
"""

from farm.crop import Crop

class Corn(Crop):
    """
    A class to represent corn, inheriting from the Crop class.

    Methods:
        water(): Increases the number of grains by 10.
    """

    def water(self):
        """
        Simulates watering the corn, increasing the number of grains by 10.
        """
        self.grains += 10

"""
--- DISREGARD EVERYTHING BELOW THIS LINE ---
This is a placeholder for the not-refactored class for the challenge version
# $DELETE_END
class Corn:
    # YOUR CODE HERE
    pass
# $DELETE_BEGIN
"""
# $DELETE_END
