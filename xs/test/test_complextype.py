import xs


class AttributeOnlyType(xs.ComplexType):
    attributes = [
        xs.Attribute("foo", xs.String),
    ]


class SequenceType(xs.ComplexType):
    content = xs.Sequence(
        xs.Element("foo", xs.String)
    )


#def test_ComplexType():
#    class PersonInfo(xs.ComplexType):
#        alive = xs.Element("alive", xs.Boolean)
#
#    p = PersonInfo()
#    p.alive = True
#
#    assert isinstance(PersonInfo.alive, xs.Element)
#    assert isinstance(p.alive, bool)


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


def test_complex_type_elements():
    obj = SequenceType()

    obj.foo = "bar"
    assert obj.to_xml() == b'<SequenceType><foo>bar</foo></SequenceType>'
