"""
Module: rice
This module contains the Rice class, which is a subclass of Crop. It represents a specific type of
crop and provides additional methods for watering and transplanting the rice to increase its grains.
"""

from farm.crop import Crop

class Rice(Crop):
    """
    A class to represent rice, inheriting from the Crop class.

    Methods:
        water(): Increases the number of grains by 5.
        transplant(): Increases the number of grains by 10.
    """

    def water(self):
        """
        Simulates watering the rice, increasing the number of grains by 5.
        """
        self.grains += 5

    def transplant(self):
        """
        Simulates transplanting the rice, increasing the number of grains by 10.
        """
        self.grains += 10
