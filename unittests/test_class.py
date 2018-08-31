import pytest
from unittests.some_class import SomeClass

# Good practices and rules about discoveries
# https://docs.pytest.org/en/latest/goodpractices.html


@pytest.mark.usefixtures("setup_for_class")
# Name must start with "Test" for pytest discovery to find it.
class TestSomeClass:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.that_class = SomeClass(2, 4)

    def test_sum(self):
        result = self.that_class.sum()
        assert result == 6

    def test_multiply(self):
        result = self.that_class.multiply()
        assert result == 8
