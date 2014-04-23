import pytest

from xs.parsers import EtreeParser
from xs.test.test_complextype import Student, EXPECTED_STUDENT_XML

def test_parse_string():

    parser = EtreeParser()
    parser.register(Student)
    student = parser.parse_string(EXPECTED_STUDENT_XML)

    assert isinstance(student, Student)
    assert student.name == "Joe Cool"
    assert student.grade == [75, 89, 66]
