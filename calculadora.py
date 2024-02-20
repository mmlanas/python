print("***********Calculadora***********")


def consulta_continuar():
    while True:
        respuesta = input("¿Desea continuar? (\'s\'/\'n\'): ").strip().lower()
        if respuesta in ["s", "si", "sí"]:
            return True
        elif respuesta in ["n", "no"]:
            print("Calculadora finalizada.")
            return False
        else:
            print("Por favor, ingresa 's' para continuar o 'n' para salir.")


def verificacion_num(numero):
    while True:
        try:
            numero = float(numero)
            if numero.is_integer():
                numero = int(numero)
            return numero
        except ValueError:
            numero = input("Ingresa un número válido: ")


def verificacion_op(operacion):
    while True:
        if operacion.strip().lower() == "suma" or operacion == "+":
            return "+"
        elif operacion.strip().lower() == "resta" or operacion == "-":
            return "-"
        elif operacion.strip().lower() == "multiplicación" or operacion.strip().lower() == "multi" or operacion.strip().lower() == "multiplicacion" or operacion == "*":
            return "*"
        elif operacion.strip().lower() == "división" or operacion.strip().lower() == "division" or operacion.strip().lower() == "div" or operacion == "/":
            return "/"
        else:
            operacion = input("Ingresa una operación básica correctamente: ")


def calcular(n1, operacion):
    while True:
        n2 = input("Ingresa otro número: ")
        n2 = verificacion_num(n2)
        if operacion == "+":
            n1 = n1 + n2
        elif operacion == "-":
            n1 = n1 - n2
        elif operacion == "*":
            n1 = n1 * n2
        elif operacion == "/":
            if n2 == 0:
                print("no se puede dividir por cero")
                continue
            else:
                n1 = n1 / n2
        print(f"El resultado es {n1}")

        if not consulta_continuar():
            return

        operacion = input(
            "Ingresa una operación: ")
        operacion = verificacion_op(operacion)


print("Operaciones básicas: \'+\', \'-\', \'*\', \'/\'")
n1 = input("Ingresa un número: ")
n1 = verificacion_num(n1)

operacion = input(
    "Ingresa una operación básica: ")

operacion = verificacion_op(operacion)

calcular(n1, operacion)
