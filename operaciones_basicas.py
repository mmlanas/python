
import verificaciones
import consultas


def calcular(n1, operacion):
    while True:
        n2 = input("Ingresa otro número: ")
        n2 = verificaciones.verificacion_num(n2)
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

        if not consultas.consulta_continuar():
            return

        operacion = input(
            "Ingresa una operación: ")
        operacion = verificaciones.verificacion_op(operacion)
