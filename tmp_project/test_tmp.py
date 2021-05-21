import importlib
from _decimal import Context


class TestDemo:
    context=Context()

    def test_import(self):
        a = importlib.import_module("hello")
        print(a.hi())





