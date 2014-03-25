"""Common testing utilities"""

import pytest

import xs


def assert_valid(type_, value):
    """Assert that `value` is a valid value for `type_`"""
    element = xs.TopLevelElement("element", type_)
    element.value = value
    assert element.value == value


def assert_invalid(type_, value):
    """Assert that `value` is an invalid value for `type_`"""
    element = xs.TopLevelElement("element", type_)
    with pytest.raises(ValueError):
        element.value = value

def assert_converts(type_, value, new_value):
    """Assert that an element of type `type_` converts `value` to `new_value`
    """
    element = xs.TopLevelElement("element", type_)
    element.value = value
    assert element.value == new_value
