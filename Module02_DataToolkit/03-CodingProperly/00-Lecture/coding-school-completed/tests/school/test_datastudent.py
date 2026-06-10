# pylint: disable=missing-docstring,missing-function-docstring

from school.datastudent import DataStudent


def test_data_student_name_capitalized():
    student = DataStudent("Name", 20)
    assert student.name == "Name"


def test_data_student_name_not_capitalized():
    student = DataStudent("name", 20)
    assert student.name == "Name"


def test_data_student_age():
    student = DataStudent("name", 20)
    assert student.age == 20


def test_data_student_language():
    student = DataStudent("name", 20)
    assert student.language == "Python"


def test_data_student_says_something():
    student = DataStudent("name", 20)
    quote = "I am a student"
    expected = "Name says: I am a student"
    assert student.says(quote) == expected


def test_data_student_from_birth_year():
    student = DataStudent.from_birth_year("name", 2000)
    assert student.name == "Name"
    assert student.age == 25  # TODO: Make this work for any year
    assert student.language == "Python"


def test_data_student_age_is_int():
    student = DataStudent("name", "20")
    assert isinstance(student.age, int)
