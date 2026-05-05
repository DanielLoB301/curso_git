# Funciones matemáticas básicas
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"
def potencia(a, b):
    return a ** b
def raiz_cuadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
def factorial(n):
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
print(sumar(5, 3))          # Salida: 8
print(restar(10, 4))       # Salida: 6
print(multiplicar(7, 6))   # Salida: 42