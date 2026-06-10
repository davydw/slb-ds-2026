# pylint: disable=too-many-instance-attributes
"""
board.py

This module defines the Board class, which is responsible for rendering and displaying the visual
representation of the farm in the Farming Diary game. It handles the layout of crops and animals,
their associated stats, and decorative elements like the sky and grass.

Classes:
    Board:
        Represents the visual board for the game, including methods to render fields, stats, and
        the overall farm display.

Functions:
    None

Usage:
    The Board class is used to create and display the farm's state. It interacts with Ref objects
    to render crops and animals, and provides a visual representation of the farm in the terminal.

Dependencies:
    - numpy: For handling matrix operations when rendering the board layout.
    - farm.helpers.ref: For managing references to crops and animals.
"""
import numpy as np
from farm.helpers.ref import Ref

class Board:
    """
    Represents the visual board for the Farming Diary game.
    Handles the rendering of fields, stats, and the overall display of the farm.
    """

    def __init__(self):
        """
        Initializes the board with dimensions, margins, and references to crops and animals.
        """
        self.board_width = 39
        self.field_rows = 2
        self.field_columns = 2
        self.margin = 3
        self.stats_width = 10

        self.corn = Ref(label="Corn", product="grains", icon="🌽", bg="🟫")
        self.rice = Ref(label="Rice", product="grains", icon="🌾", bg="🟫")
        self.cow = Ref(label="Cow", product="milk", icon="🐮", bg="🟥", roof=True)
        self.chicken = Ref(label="Chicken", product="eggs", icon="🐔", bg="🟥", roof=True)

    def render_field(self, ref):
        """
        Renders the field for a given reference (e.g., crop or animal).

        Args:
            ref (Ref): The reference object to render.

        Returns:
            list: A list of strings representing the field rows.
        """
        slots = self.field_rows * self.field_columns
        f = [ref.get_icon(i) for i in range(slots)]
        return ["".join(f[i:i + self.field_columns]) for i in range(0, len(f), self.field_columns)]

    def render_stat(self, label, value):
        """
        Renders a single stat line with a label and value.

        Args:
            label (str): The label for the stat.
            value (int): The value of the stat.

        Returns:
            str: A formatted string representing the stat.
        """
        return f" {label}{str(value).rjust(self.stats_width - len(label), '.')}"

    def render_block(self, ref):
        """
        Renders a block for a given reference, including its field and stats.

        Args:
            ref (Ref): The reference object to render.

        Returns:
            list: A list of strings representing the block.
        """
        f = self.render_field(ref)
        f[0] += self.render_stat(ref.label, ref.count)
        f[1] += self.render_stat(ref.nice_product(), ref.product_count())

        if ref.roof:
            f.insert(0, "/⚪️\\".ljust(self.stats_width + 5))
            f.insert(0, " __".ljust(self.stats_width + 5))
        return f

    def display_sky(self, string=" " * 39):
        """
        Displays a line of the sky with a given string.

        Args:
            string (str): The string to display in the sky. Defaults to empty spaces.
        """
        print(f"\033[48;5;33;1m{string}\033[0m")

    def display_grass(self, string=" " * 39):
        """
        Displays a line of grass with a given string.

        Args:
            string (str): The string to display in the grass. Defaults to empty spaces.
        """
        print(f"\033[48;5;22;38;255;0m{string}\033[0m")

    def display_title(self):
        """
        Displays the title of the game with decorative elements.
        """
        print("\n\n")
        self.display_sky()
        self.display_sky()
        self.display_sky("~  Farming Diary  ~".center(self.board_width))
        self.display_sky()
        self.display_sky("🌳🌳🌳🌳 🌳       🏡        🌳 🌳🌳🌳🌳")

    def display_main(self, *items):
        """
        Displays the main content of the board, including crops and animals.

        Args:
            *items (list): Lists of strings representing blocks to display.
        """
        rows = max(len(item) for item in items)
        margin = [" " * self.margin] * rows

        columns = [margin]
        for item in items:
            columns.append(item)
            columns.append(margin)

        matrix = np.array(columns).T
        for row in matrix:
            self.display_grass("".join(row))

    def display(self):
        """
        Displays the entire board, including the title, crops, and animals.
        """
        self.display_title()
        self.display_grass()
        self.display_main(self.render_block(self.corn), self.render_block(self.rice))
        self.display_main(self.render_block(self.cow), self.render_block(self.chicken))
        self.display_grass()
        print("\n\n")
