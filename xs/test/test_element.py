import xs


def test_create_simple_elements():
    name = xs.Element("lastname", xs.String, u"Refnes")
    assert name.value == u"Refnes"
    assert name.to_xml() == "<lastname>Refnes</lastname>"


def test_create_element_instance():
    name_element = xs.Element("lastname", xs.String)

    name = name_element(u"Refnes")
    assert name.value == u"Refnes"
    assert name.to_xml() == "<lastname>Refnes</lastname>"
