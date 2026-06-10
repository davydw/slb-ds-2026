"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

from farm.corn import Corn
# $DELETE_BEGIN
from farm.rice import Rice
# $DELETE_END

print("\n\n📝 Day One: Corn")

# 1. Instantiate a corn crop
# $CHALLENGIFY_BEGIN
corn = Corn()
# $CHALLENGIFY_END

# 2. Water the corn crop
# $CHALLENGIFY_BEGIN
corn.water()
# $CHALLENGIFY_END

# 3. Print "The corn crop produced ## grains"
# $CHALLENGIFY_BEGIN
print(f"The corn crop produced {corn.grains} grains")
# $CHALLENGIFY_END

# 4. Print "The corn crop is ripe" or "The corn crop is not ripe"
# $CHALLENGIFY_BEGIN
print(f"The corn crop is {'ripe' if corn.ripe() else 'not ripe'}")
# $CHALLENGIFY_END

print("\n\n📝 Day Two: Rice")

# 1. Instantiate a rice crop
# $CHALLENGIFY_BEGIN
rice = Rice()
# $CHALLENGIFY_END

# 2. Water the rice crop
# $CHALLENGIFY_BEGIN
rice.water()
# $CHALLENGIFY_END

# 3. Transplant the rice crop
# $CHALLENGIFY_BEGIN
rice.transplant()
# $CHALLENGIFY_END

# 4. Print "The rice crop produced ## grains"
# $CHALLENGIFY_BEGIN
print(f"The rice crop produced {rice.grains} grains")
# $CHALLENGIFY_END

# 5. Print "The rice crop is ripe" or "The rice crop is not ripe"
# $CHALLENGIFY_BEGIN
print(f"The rice crop is {'ripe' if rice.ripe() else 'not ripe'}")
# $CHALLENGIFY_END
