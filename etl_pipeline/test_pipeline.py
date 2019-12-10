"""Unit tests for the pipeline functions. Uses pytest
"""

from etl_pipeline.etl_util import __match_location_to_state, __remove_symbols_from_description
from pyspark.sql.types import NullType
import pytest
import string


def test_match_location_to_state():
    assert (__match_location_to_state("Seattle, WA") == "WA")
    assert (__match_location_to_state("Palo Alto, CA") == "CA")


def test_match_location_to_state_hyphen():
    assert (__match_location_to_state("Portland -- OR") == "OR")
    assert (__match_location_to_state("Albany -- NY") == "NY")


def test_match_location_to_state_long_state_name():
    assert (__match_location_to_state("Madison_Wisconsin") == "WI")


def test_match_location_to_state_invalid_state_name():
    assert (__match_location_to_state("Richmond -- Virg") == None)


def test_match_location_to_state_missing_state():
    assert (__match_location_to_state("Richmond") == None)


def test_match_location_to_state_missing_value():
    assert (__match_location_to_state("") == None)
    assert (__match_location_to_state(None) == None)


def test_remove_symbols_from_description():
    test_data = [
        ("in \"\"Inspiring Generations through Knowledge and Discovery.\"\" EOE\"",
         "in Inspiring Generations through Knowledge and Discovery EOE"),
        ("ASP.NET MVC (C#), HTML, JavaScript.-Experience building or maintai",
         "ASPNET MVC C HTML JavaScriptExperience building or maintai")
    ]

    for current_test in test_data:
        assert (__remove_symbols_from_description(
            current_test[0]) == current_test[1])
