"""
Run:
>pytest -v -s unittests/test_class.py
"""

class SomeClass:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        return self.number1 + self.number2

    def multiply(self):
        return self.number1 * self.number2
