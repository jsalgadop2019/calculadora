
from calculadora.app.operaciones import potencia

# 2) Buenas practicas
import pytest


def obtener_datos_test_potencia():
    return [(2, 3, 8), (4, 2, 16), (3, 3, 27)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_potencia())
def test_potencia_parametrize(num1, num2, esperado):
    assert potencia(num1, num2) == esperado
