class Student():
    """
    >>> from school.student import Student
    >>> margo = Student("margo", 34)
    >>> margo.name
    'Margo'
    >>> margo.age
    34
    >>> margo.language
    'Ruby'
    >>> margo.says("I was a student of batch 7!")
    'Margo says: I was a student of batch 7!'
    """

    # Class attribute
    language = "Ruby"

    # Constructor
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    # Instance method
    def says(self, quote):
        return f"{self.name} says: {quote}"

    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year  # TODO: Make this work for any year
        return cls(name, age)
