import math
from typing import Union

Number = Union[int, float]

def suma(a: Number, b: Number) -> Number:
	"""Devuelve la suma de a y b."""
	return a + b

def resta(a: Number, b: Number) -> Number:
	"""Devuelve la resta a - b."""
	return a - b

def multiplicacion(a: Number, b: Number) -> Number:
	"""Devuelve el producto de a y b."""
	return a * b

def division(a: Number, b: Number) -> Number:
	"""Devuelve la división a / b. Lanza ZeroDivisionError si b es 0."""
	if b == 0:
		raise ZeroDivisionError("División por cero")
	return a / b

def raiz_cuadrada(x: Number) -> float:
	"""Devuelve la raíz cuadrada de x. Lanza ValueError si x es negativo."""
	if x < 0:
		raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
	return math.sqrt(x)

