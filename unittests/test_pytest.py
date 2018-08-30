import pytest

"""

Run all tests under path:
> pytest [path]

Run tests in module:
> pytest test_pytest.py   

Run only test_1 method in module test_pytest.py
> pytest test_pytest.py::test_1

Arguments:
    -s print statements
    -v verbose

Can use wildcard * in paths. 
    Ex: pytest test_pytest*.py

"""


@pytest.fixture()
def pyt_fixture():
    number = 10
    return number


@pytest.yield_fixture()
def pyt_yield_fixture():
    print("start", end=' > ')
    yield
    print(" > end", end='')


def test_1(pyt_fixture):
    assert pyt_fixture == 10


def test_2(pyt_yield_fixture):
    assert 50 > 10

