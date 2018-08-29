import pytest

"""
Got to terminal and run: "pytest -v"
"""


@pytest.fixture()
def setup():
    number = 10
    return number


def test_1(setup):
    assert setup == 10


def test_2(setup):
    assert 50 > setup
