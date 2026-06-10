"""
interface.py

This module serves as the main entry point for the Farming Diary game. It allows users to interact
with the game by performing various actions such as planting crops, watering them, adding animals,
feeding them, and quitting the game.

Classes:
    None

Functions:
    main():
        Runs the main game loop, allowing the user to interact with the farm by choosing actions.

Usage:
    Run this script to start the Farming Diary game. The user will be prompted to pick actions to
    manage their farm, including planting crops, adding animals, and maintaining them.

Dependencies:
    - helpers.board: For displaying the farm's state.
    - farm.rice: For creating and managing rice crops.
    - farm.corn: For creating and managing corn crops.
    - farm.cow: For creating and managing cows.
    - farm.chicken: For creating and managing chickens.
    - random: For generating random values (e.g., chicken gender).
"""
import random
from farm.helpers.board import Board
from farm.rice import Rice
from farm.corn import Corn
from farm.cow import Cow
from farm.chicken import Chicken

def main():
    """
    Main function to run the farming diary game.
    Allows the user to perform actions such as planting crops, watering them,
    adding animals, feeding them, and quitting the game.
    """
    crops = []
    animals = []

    action = ""
    while action != "quit":

        # Display the state of the farm
        Board().display()

        print("Pick an action: [corn | rice | water | cow | chicken | feed | quit]")
        action = input("> ").strip()

        if action == "corn":
            print("Let's plant corn crops!")
            crops.append(Corn())
        elif action == "rice":
            print("Rice crops today!")
            crops.append(Rice())
        elif action == "water":
            print("Watering crops...")
            for crop in crops:
                crop.water()
        elif action == "cow":
            print("It's cow time!")
            animals.append(Cow())
        elif action == "chicken":
            print("Let's add a chicken!")
            gender = random.choice(["female", "male"])
            print(f"The chicken is a {gender}")
            animals.append(Chicken(gender))
        elif action == "feed":
            print("Feeding animals...")
            for animal in animals:
                animal.feed()
        elif action == "quit":
            print("See you next time")
        else:
            print("I don't know what you mean...")

if __name__ == "__main__":
    main()
