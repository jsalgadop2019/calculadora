
from calculadora.app.operaciones import raiz


# 2) Buenas practicas
import pytest


def obtener_datos_test_raiz():
    return [(125, 3, 5), (64, 3, 4), (16, 4, 2)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_raiz())
def test_raiz_parametrize(num1, num2, esperado):
    assert suma(num1, num2) == esperado