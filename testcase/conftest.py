# yield前代码相当于setup,yield后代码相当于teardown ,yield相当于return
# 若autouse=True则相当于在各方法中自动调用，scope定义fixture的作用域
import pytest

from pythoncodings.calculator import Calculator


@pytest.fixture(autouse=True,scope="class")
def get_calc():
    calc = Calculator()
    print("初始化开始")
    yield calc
    print("初始化结束")

