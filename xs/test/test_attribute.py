import pytest

import xs


class ExampleCT(xs.ComplexType):
    pass


def test_attribute_must_be_simple_type():
    with pytest.raises(TypeError):
        attribute = xs.Attribute("attr", ExampleCT)
