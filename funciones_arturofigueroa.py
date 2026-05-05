# Operaciones
a = 0
b = 0

a = int(input("Ingrese un numero a: "))
b = int(input("Ingrese numero b: "))

def operaciones(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    potencia = a **b
    
    print(f"Suma: {suma}\nResta: {resta}\nMultiplicacion: {multiplicacion}\nDivision: {division}\nPotencia{potencia}")
    
operaciones(a,b)