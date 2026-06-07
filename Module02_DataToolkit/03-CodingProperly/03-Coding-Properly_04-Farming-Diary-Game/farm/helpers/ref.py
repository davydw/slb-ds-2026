# pylint: disable=unused-import
"""
ref.py

This module defines the Ref class, which is responsible for managing references to crops or animals
in the Farming Diary game. It provides functionality to handle attributes, icons, and
product-related calculations for the objects in the game.

Classes:
    Ref:
        Represents a reference object for crops or animals, allowing for the retrieval of icons,
        product counts, and other attributes.

Functions:
    None

Usage:
    The Ref class is used to manage and interact with instances of crops or animals in the game.
    It dynamically identifies instances of a given class, retrieves their attributes, and calculates
    their product-related statistics.

Dependencies:
    - gc: For accessing all objects in memory to find instances of specific classes.
    - farm.chicken: For managing chicken instances.
    - farm.cow: For managing cow instances.
    - farm.corn: For managing corn instances.
    - farm.rice: For managing rice instances.
"""
import gc
from farm.chicken import Chicken
from farm.cow import Cow
from farm.corn import Corn
from farm.rice import Rice


class Ref:
    """
    Represents a reference object for crops or animals in the Farming Diary game.
    Handles attributes, icons, and product-related calculations.
    """

    def __init__(self, **kwargs):
        """
        Initializes the Ref object with attributes such as label, product, icon, and background.

        Args:
            attributes (dict): A dictionary containing the attributes of the reference.
        """
        self.label = kwargs.get("label")
        self.product = kwargs.get("product")
        self.icon = kwargs.get("icon")
        self.bg = kwargs.get("bg")
        self.roof = kwargs.get("roof", False)
        self.items = self.select_instances(self.label)
        self.count = len(self.items)

    def is_a_class(self, class_name):
        """
        Checks if a given class name exists in the current Python environment.

        Args:
            class_name (str): The name of the class to check.

        Returns:
            bool: True if the class exists, False otherwise.
        """
        return class_name in globals()

    def select_instances(self, class_name):
        """
        Selects all instances of a given class name from the current Python environment.

        Args:
            class_name (str): The name of the class to find instances of.

        Returns:
            list: A list of instances of the specified class.
        """
        if self.is_a_class(class_name):
            cls = globals()[class_name]
            return [obj for obj in gc.get_objects() if isinstance(obj, cls)]
        return []

    def get_icon(self, i):
        """
        Gets the icon for a given item. Returns the icon if the item's class matches the label,
        otherwise returns the background.

        Args:
            item (object): The item to get the icon for.

        Returns:
            str: The icon or background string.
        """
        return self.icon if i < self.count else self.bg

    def get_product(self, item):
        """
        Gets the product value for a given item if it has the product attribute.

        Args:
            item (object): The item to get the product value for.

        Returns:
            int: The product value, or 0 if the item does not have the product attribute.
        """
        return getattr(item, self.product, 0)

    def product_count(self):
        """
        Calculates the total product count for all items.

        Returns:
            int: The total product count, or 0 if no items have the product attribute.
        """
        if self.count > 0 and any(hasattr(item, self.product) for item in self.items):
            return sum(self.get_product(item) for item in self.items)
        return 0

    def nice_product(self):
        """
        Returns the product name as a string.

        Returns:
            str: The product name.
        """
        return str(self.product)
