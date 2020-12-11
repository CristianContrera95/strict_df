import pytest
from src.strictdf.utils.dtypes import str_check_float, str_check_bool, str_check_int


@pytest.mark.parametrize(
    'string, expected',
    [
        ("", False),
        (".", False),
        ("2.0", False),
        ("1.5", False),
        ("a", False),
        ("adsada", False),
        ("0.5", False),
        ("2", False),
        ("1.0", True),
        ("1.000000000", True),
        ("0", True),
        (".0", True),
        ("True", True),
        ("true", True),
        ("False", True),
        ("False", True),
        ("t", True),
        ("1", True),
        ("f", True),
        ("t.", True),
    ]
)
def test_str_check_bool(string, expected):

    assert bool(str_check_bool(string)) == expected


@pytest.mark.parametrize(
    'string, expected',
    [
        ("", False),
        (".", False),
        ("212.", True),
        ("2.0", True),
        ("1.5", False),
        ("a", False),
        ("adsada", False),
        (".5", False),
        ("2", True),
        ("1.0", True),
        ("1.000000000", True),
        ("0", True),
        (".0", True),
        ("True", False),
        ("true", False),
    ]
)
def test_str_check_int(string, expected):

    assert bool(str_check_int(string)) == expected


@pytest.mark.parametrize(
    'string, expected',
    [
        ("", False),
        (".", False),
        ("212.", True),
        ("2.0", True),
        ("1.5", True),
        ("a", False),
        ("adsada", False),
        (".5", True),
        ("2", False),
        ("1.0", True),
        ("1.000000000", True),
        ("0", False),
        (".0", True),
        ("True", False),
        ("true", False),
    ]
)
def test_str_check_float(string, expected):

    assert bool(str_check_float(string)) == expected
