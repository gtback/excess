import pytest

import xs


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
    assert obj.to_xml() == b'<AttributeOnlyType foo="bar" />'


def test_cannot_set_unnnamed_attr():
    p = PersonInfo()
    p.firstname = "Franklin"
    p.lastname = "Roosevelt"

    # "middlename" is not an element defined on our PersonInfo model.
    with pytest.raises(AttributeError):
        p.middlename = "Delano"


def test_complex_type_elements():
    obj = SequenceType()

    obj.foo = "bar"
    assert obj.to_xml() == b'<SequenceType><foo>bar</foo></SequenceType>'


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

    assert p.to_xml() == b"".join(xmlstr.split())

