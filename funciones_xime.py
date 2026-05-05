def suma(a, b)
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b
print(suma(5, 3))            # 8
print(resta(5, 3))           # 2
print(multiplicacion(5, 3))  # 15
print(division(6, 3))        # 2.0

