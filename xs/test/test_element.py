import xs


def test_create_simple_elements():
    name = xs.Element("lastname", xs.String, value="Refnes")
    assert name.value == "Refnes"
    assert name.to_xml() == b"<lastname>Refnes</lastname>"


def test_create_element_instance():
    name_element = xs.Element("lastname", xs.String)

    name = name_element("Refnes")
    assert name.value == "Refnes"
    assert type(name.value) == xs.compat.str
    assert name.to_xml() == b"<lastname>Refnes</lastname>"
