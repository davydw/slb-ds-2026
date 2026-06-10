# pylint: disable=too-few-public-methods
# $CHALLENGIFY_BEGIN
"""
Module: crop
This module contains the Crop class, which represents a crop with grains and provides
functionality to check if the crop is ripe.
"""

class Crop:
    """
    A class to represent a crop.

    Attributes:
        grains (int): The number of grains the crop has.
    """

    def __init__(self):
        """
        Initializes a Crop instance with zero grains.
        """
        self.grains = 0

    def ripe(self):
        """
        Checks if the crop is ripe.

        Returns:
            bool: True if the crop has 15 or more grains, False otherwise.
        """
        return self.grains >= 15
# $CHALLENGIFY_END
