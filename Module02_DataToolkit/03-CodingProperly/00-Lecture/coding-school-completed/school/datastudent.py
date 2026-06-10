from school.student import Student


class DataStudent(Student):
    language = "Python"

    def __init__(self, name, age):
        super().__init__(name, int(age))

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year  # TODO: Make this work for any year
        return cls(name, age)
