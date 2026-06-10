# pylint: disable=missing-docstring,missing-function-docstring

from school.student import Student


def test_student_name_capitalized():
    student = Student("Name", 20)
    assert student.name == "Name"


def test_student_name_not_capitalized():
    student = Student("name", 20)
    assert student.name == "Name"


def test_student_age():
    student = Student("name", 20)
    assert student.age == 20


def test_student_language():
    student = Student("name", 20)
    assert student.language == "Ruby"


def test_student_says_something():
    student = Student("name", 20)
    quote = "I am a student"
    expected = "Name says: I am a student"
    assert student.says(quote) == expected


def test_student_from_birth_year():
    student = Student.from_birth_year("name", 2000)
    assert student.name == "Name"
    assert student.age == 25  # TODO: Make this work for any year
    assert student.language == "Ruby"
