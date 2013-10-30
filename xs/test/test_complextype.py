import xs


def test_ComplexType():
    class PersonInfo(xs.ComplexType):
        alive = xs.Element("alive", xs.Boolean)

    p = PersonInfo()
    p.alive = True

    assert isinstance(PersonInfo.alive, xs.Element)
    assert isinstance(p.alive, bool)
