
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
