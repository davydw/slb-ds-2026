"""
This script simulates a farming diary where animals interact and perform actions.

It demonstrates the behavior of different animals (e.g., cows and chickens) by:
- Making them "talk" to display their characteristic sounds.
- Feeding them to increase their energy and produce resources (e.g., milk or eggs).
- Printing the results of their actions.

Classes used:
- Cow: Represents a cow that produces milk.
- Chicken: Represents a chicken that lays eggs (if female) and makes gender-specific sounds.
"""

from farm.cow import Cow
from farm.chicken import Chicken

print("\n\n📝 Day Three: Animals Talk")

# 1. Read the code and gather some clues to code the classes
cow = Cow()
female_chicken = Chicken('female')
male_chicken = Chicken('male')

print(f"The cow says {cow.talk()}")
print(f"The female chicken says {female_chicken.talk()}")
print(f"The male chicken says {male_chicken.talk()}")

print("\n\n📝 Day Four: Feed The Animals")

# 1. Store all your animals in an `animals` list
# $CHALLENGIFY_BEGIN
animals = [cow, female_chicken, male_chicken]
# $CHALLENGIFY_END

# 2. Call the `feed` method on each animal (use a loop on the list)
# $CHALLENGIFY_BEGIN
for animal in animals:
    animal.feed()
# $CHALLENGIFY_END

# 3. Replace the TODOs

# 4. Print the following 3 lines:
# "The cow produced ## liters of milk"
# "The female chicken produced ## eggs"
# "The male chicken produced ## eggs"
# $CHALLENGIFY_BEGIN
print(f"The cow produced {cow.milk} liters of milk")
print(f"The female chicken produced {female_chicken.eggs} eggs")
print(f"The male chicken produced {male_chicken.eggs} eggs")
# $CHALLENGIFY_END
