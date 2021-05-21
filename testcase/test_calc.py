import yaml

from pythoncodings.calculator import Calculator
import pytest


def get_data():
    with open("data.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas["add"]["datas"]
    sub_datas = datas["sub"]["datas"]
    mul_datas = datas["mul"]["datas"]
    div_datas = datas["div"]["datas"]
    add_datas_ids = datas["add"]["ids"]
    sub_datas_ids = datas["sub"]["ids"]
    mul_datas_ids = datas["mul"]["ids"]
    div_datas_ids = datas["div"]["ids"]

    # print(datas)
    return [add_datas, add_datas_ids, sub_datas, sub_datas_ids, mul_datas, mul_datas_ids, div_datas, div_datas_ids]


class TestCal:
    @pytest.mark.parametrize("a,b,expect", [
        get_data()[0], get_data()[1], get_data()[2]
    ])
    def test_add(self, get_calc, a, b, expect):
        result = get_calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expectd", [
        [1, 0, 'ERROR'], [4, 2, 2], [0.4, 0.1, 4]
    ])
    def test_div(self, get_calc, a, b, expectd):
        result = get_calc.div(a, b)
        assert result == expectd

    def test_mul(self, get_calc, a, b, result):
        expect = get_calc.mul(a, b)
        assert expect == result
