import pytest

import xs
from xs.test import uglify


class AttributeOnlyType(xs.ComplexType):
    attributes = [
        xs.Attribute("foo", xs.String),
    ]


class SequenceType(xs.ComplexType):
    content = xs.Sequence(
        xs.Element("foo", xs.String)
    )


class PersonInfo(xs.ComplexType):
    content = xs.Sequence(
        xs.Element("firstname", xs.String),
        xs.Element("lastname", xs.String)
    )


class Student(xs.ComplexType):
    content = xs.Sequence(
        xs.Element("name", xs.String),
        xs.Element("course", xs.String, max_occurs=2),
        xs.Element("grade", xs.Integer, max_occurs=xs.UNBOUNDED),
    )


def test_attribute_only_type():
    assert len(AttributeOnlyType.attributes) == 1
    attrs = AttributeOnlyType._component_dict()
    assert type(attrs) == dict
    assert len(attrs) == 1

    attr = attrs["foo"]
    assert type(attr) == xs.Attribute
    assert attr.name == "foo"
    assert attr.type_ == xs.String


def test_complex_type_attributes():
    obj = AttributeOnlyType()
    assert type(obj._fields) == dict
    obj.foo = "bar"
    assert xs.serialize(obj) == b'<AttributeOnlyType foo="bar" />'


def test_cannot_set_unnnamed_attr():
    p = PersonInfo()
    p.firstname = "Franklin"
    p.lastname = "Roosevelt"

    # "middlename" is not an element defined on our PersonInfo model.
    with pytest.raises(AttributeError):
        p.middlename = "Delano"


EXPECTED_STUDENT_XML = uglify(b"""
    <Student>
        <name>Joe Cool</name>
        <grade>75</grade>
        <grade>89</grade>
        <grade>66</grade>
    </Student>""")


def test_min_occurs():
    student = Student()
    student.grade = [95]

    with pytest.raises(ValueError):
        xs.serialize(student)

def test_max_occurs_unbounded():
    s = Student()
    s.name = "Joe Cool"
    s.grade.append(75)
    s.grade.append(89)
    s.grade.append(66)

    assert EXPECTED_STUDENT_XML == xs.serialize(s)


def test_max_occurs_bounded():
    s = Student()
    s.name = "Joe Cool"
    s.course.append("History")
    s.course.append("Algebra")
    with pytest.raises(IndexError):
        s.course.append("English")


def test_set_list():
    s = Student()
    s.name = "Joe Cool"
    s.grade = [75, 89, 66]

    assert EXPECTED_STUDENT_XML == xs.serialize(s)


def test_set_single():
    s = Student()
    s.name = "Joe Cool"
    s.grade = 95

    expected = b"<Student><name>Joe Cool</name><grade>95</grade></Student>"
    assert expected == xs.serialize(s)


def test_complex_type_elements():
    obj = SequenceType()

    obj.foo = "bar"
    assert xs.serialize(obj) == b'<SequenceType><foo>bar</foo></SequenceType>'


def test_top_level_element_with_complex_type():
    p = xs.TopLevelElement("employee", PersonInfo)

    assert p.name == "employee"
    assert p.type_ == PersonInfo
    assert p.value == None

    p.firstname = "John"
    p.lastname = "Smith"

    xmlstr = b"""
    <employee>
        <firstname>John</firstname>
        <lastname>Smith</lastname>
    </employee>
    """

    assert xs.serialize(p) == b"".join(xmlstr.split())
