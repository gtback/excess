import pytest

import xs


class ExampleCT(xs.ComplexType):
    pass


def test_attribute_must_be_simple_type():
    invalid_attribute_types = [
            ExampleCT,  # Can't use a ComplexType as an attribute
            xs.Attribute,  # Don't use the Attribute class itself
            int,  # Don't allow Python native types (use 'xs' equivalents)
            bool,
    ]

    # Each of these should raise a TypeError
    for invalid_type in invalid_attribute_types:
        with pytest.raises(TypeError):
            attribute = xs.Attribute("attr", invalid_type)

    valid_attribute_types = [
            xs.Boolean,
            xs.String,
    ]

    # None of these should raise an error
    for valid_type in valid_attribute_types:
        attribute = xs.Attribute("attr", valid_type)
