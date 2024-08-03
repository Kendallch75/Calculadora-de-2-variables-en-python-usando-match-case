# calculadora en python con 2 variables
print("Hola, esto es una calculadora para operaciones aritméticas de dos variables\nSelecciona tu operación\n1 = Suma\n2 = Resta\n3 = Multiplicación\n4 = División\n5 = Módulo")
o = int(float("Ingrese la operación: "))
x = int(float("Ingrese la primera variable: "))
y = int(float("Ingrese la segunda variable: "))


def calculadora(o, x, y):
    match o:
        case 1:
            return f"El resultado de la suma es: {x + y}"
        case 2:
            return f"El resultado de la resta es: {x - y}"
        case 3:
            return f"El resultado de la multiplicación es: {x * y}"
        case 4:
            if y == 0:
                return "Error: No se puede dividir por cero."
            return f"El resultado de la división es: {x / y}"
        case 5:
            if y == 0:
                return "Error: No se puede calcular el módulo con cero."
            return f"El resultado del módulo es: {x % y}"
        case _:
            return "Operación no válida."


print(calculadora(o, x, y))
