
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
