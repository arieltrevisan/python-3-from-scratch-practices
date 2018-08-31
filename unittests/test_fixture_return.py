import pytest

"""
Run:
>pytest -v -s unittests/test_fixture_return.py --arg1 bye
"""


@pytest.mark.usefixtures("setup_fixture_return")
class TestFixtureReturn:

    def test_fixture_return(self):
        print("Value: ", self.value_rtn)
        assert 0 < self.value_rtn < 50
