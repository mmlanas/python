from funciones_calculadora import calcular
from verificaciones import *

print("***********Calculadora***********")


print("Operaciones básicas: \'+\', \'-\', \'*\', \'/\'")
n1 = input("Ingresa un número: ")
n1 = verificacion_num(n1)

operacion = input(
    "Ingresa una operación básica: ")

operacion = verificacion_op(operacion)

calcular(n1, operacion)
