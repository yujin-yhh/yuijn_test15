from pythoncodings.calculator import Calculator
import pytest


class TestCal:
    def setup_class(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.cal.add(1, 2)
        assert result == 3

    @pytest.mark.parametrize("a,b,expectd", [
        [1, 0, 'ERROR'], [4, 2, 2], [0.4, 0.1, 4]
    ])
    def test_div(self, a, b, expectd):
        result = self.calc.div(a, b)
        assert result == expectd
