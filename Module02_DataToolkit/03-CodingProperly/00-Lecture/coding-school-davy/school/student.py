class Student:
    # Class attribute(s)
    language="ruby"

    # Constructor - initalizing a class
    # self = a keyword to reference an object
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def says(self, something):
        print(f"{self.name.capitalize()} says {something}")
