import pytest
from calculadora import Calculadora

def test_sumar():
    calc = Calculadora()
    assert calc.sumar(3, 5) == 8
    assert calc.sumar(-1, 1) == 0

def test_restar():
    calc = Calculadora()
    assert calc.restar(10, 5) == 5

def test_multiplicar():
    calc = Calculadora()
    assert calc.multiplicar(3, 4) == 12

def test_dividir():
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5
    with pytest.raises(ValueError):
        calc.dividir(10, 0)
