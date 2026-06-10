"""
This module defines the EngStudent class, which represents a student in the Data
Engineering course at Le Wagon.

Classes
-------
EngStudent
    A class representing a student with attributes for name and age, and
    methods for speaking and creating instances based on birth year.
"""

from datetime import date
from typing import Self


class EngStudent:
    """
    A class to represent an engineering student.

    Attributes
    ----------
    language : str
        The class' language.

    Methods
    -------
    __init__(name, age):
        Initializes the EngStudent instance with name and age.
    says(quote):
        Returns a string with the student's name and the given quote.
    from_birth_year(name, birth_year):
        Class method to create an EngStudent instance using the birth year to
        calculate age.
    """

    language = "Python"

    def __init__(self, name, age):
        """
        Initializes a new instance of the class.
        Parameters
        ----------
        name : str
            The name of the student.
        age : int
            The age of the student.
        """
        self.name = name.capitalize()
        self.age = age

    def says(self, quote):
        """
        Returns a formatted string with the student's name and the given quote.

        Parameters
        ----------
        quote : str
            The quote that the student says.

        Returns
        -------
        str
            A string in the format "{name} says: {quote}".
        """
        return f"{self.name} says: {quote}"

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> Self:
        """
        Create an instance of the class using the birth year.

        Parameters
        ----------
        cls : type
            The class itself.
        name : str
            The name of the student.
        birth_year : int
            The birth year of the student.

        Returns
        -------
        object
            An instance of the class with the calculated age.
        """
        age = date.today().year - birth_year
        return cls(name=name, age=age)


if __name__ == "__main__":
    paul = EngStudent("paul", 34)
    print(paul.name)
    print(paul.age)
    print(paul.language)
    print(paul.says("I was a student of batch 1769!"))
    paul = EngStudent.from_birth_year("paul", "2000")
