import pytest

import xs


def test_create_top_level_element():
    name = xs.TopLevelElement("lastname", xs.String, value="Refnes")
    assert name.value == "Refnes"
    assert name.to_xml() == b"<lastname>Refnes</lastname>"


def test_create_top_level_element_from_element():
    name_element = xs.Element("lastname", xs.String)
    name = name_element("Refnes")

    assert isinstance(name, xs.TopLevelElement)
    assert name.value == "Refnes"
    assert type(name.value) == xs.compat.str
    assert name.to_xml() == b"<lastname>Refnes</lastname>"


def test_error_when_exporting_empty_top_level_element():
    name_element = xs.TopLevelElement("lastname", xs.String)

    with pytest.raises(ValueError):
        name_element.to_xml()
