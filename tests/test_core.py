import pytest

from calc import add, div


def test_add():
    assert add(2, 3) == 5

def test_div_ok():
    assert div(10, 2) == 5

def test_div_zero():
    with pytest.raises(ValueError):
        div(10, 0)
