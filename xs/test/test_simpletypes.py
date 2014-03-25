from datetime import date

import pytest

from xs import Boolean, Date, Integer, PositiveInteger, TopLevelElement
from xs.test import assert_valid, assert_invalid, assert_converts

def test_Boolean_from_xml():
    assert Boolean.from_xml("0") == False
    assert Boolean.from_xml("1") == True
    assert Boolean.from_xml("true") == True
    assert Boolean.from_xml("false") == False


def test_Boolean_to_xml():
    assert Boolean.to_xml(True) == "true"
    assert Boolean.to_xml(False) == "false"


def test_valid_Integer():
    for value in [1, 0, 100, -5]:
        assert_valid(Integer, value)

    assert_converts(Integer, "1", 1)


def test_invalid_Integer():
    #TODO: What should we do about 1.5? Python's int() will silently convert
    # to 1.
    for value in ["a"]:
        assert_invalid(Integer, value)


def test_valid_PositiveInteger():
    assert_valid(PositiveInteger, 1)


def test_invalid_PositiveInteger():
    for value in [0, -1]:
        assert_invalid(PositiveInteger, value)


DATE_PAIRS = [
    ('0001-01-01', date(1, 1, 1)),
    ('2014-01-30', date(2014, 1, 30)),
    ('2013-12-31', date(2013, 12, 31)),
]


INVALID_DATES = [
    '0000-01-01',  # Year 0000 is invalid
    '10000-01-01',  # Year 10000 is invalid
    '1999-00-01',  # Month 00 is invalid
    '2000-13-01',  # Month 13 is invalid
    '2001-04-00',  # Day 00 is invalid
    '2002-07-35',  # Day 35 is invalid
    '2003-02-29',  # Day 29 is invalid in February 2003
]



def test_Date_from_xml():
    for (xml_date, python_date) in DATE_PAIRS:
        assert Date.from_xml(xml_date) == python_date


def test_Date_to_xml():
    for (xml_date, python_date) in DATE_PAIRS:
        assert Date.to_xml(python_date) == xml_date


def test_invalid_dates():
    for d in INVALID_DATES:
        with pytest.raises(ValueError):
            Date.from_xml(d)
