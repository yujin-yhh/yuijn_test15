from pythoncodings.calculator import Calculator
import pytest


class TestCal:
    def test_add(self):
        cal = Calculator()
        result = cal.add(1, 2)
        assert result == 3
