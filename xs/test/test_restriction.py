import pytest

import xs


class MaxExclusive100(xs.Restriction, xs.PositiveInteger):
    max_exclusive = 100


def test_positive_integer_restriction():
    element = xs.TopLevelElement("example", MaxExclusive100)
    element.value = 100
    assert b"<example>100</example>" == element.to_xml()
    with pytest.raises(ValueError):
        element.value = 101

