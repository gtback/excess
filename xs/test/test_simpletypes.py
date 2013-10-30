from xs import Boolean


def test_Boolean_from_xml():
    assert Boolean.from_xml("0") == False
    assert Boolean.from_xml("1") == True
    assert Boolean.from_xml("true") == True
    assert Boolean.from_xml("false") == False


def test_Boolean_to_xml():
    assert Boolean.to_xml(True) == "true"
    assert Boolean.to_xml(False) == "false"
